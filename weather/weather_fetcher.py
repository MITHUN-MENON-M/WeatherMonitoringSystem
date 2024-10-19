# weather/weather_fetcher.py

import requests
from .models import Weather
from .database import db
from flask import current_app
import logging

logger = logging.getLogger(__name__)

def fetch_weather_data():
    API_KEY = current_app.config['API_KEY']
    CITIES = current_app.config['CITIES']
    for city in CITIES:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
        response = requests.get(url)
        data = response.json()
        if data.get('cod') != 200:
            logger.error(f"Failed to fetch data for {city}: {data.get('message', 'No message')}")
            continue
        main = data['weather'][0]['main']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        dt = data['dt']
        logger.info(f"Fetched data for {city}: Temp={temp}, Main={main}")
        weather = Weather(city=city, main=main, temp=temp, feels_like=feels_like, dt=dt)
        db.session.add(weather)
    db.session.commit()
    logger.info("Data fetching complete.")
