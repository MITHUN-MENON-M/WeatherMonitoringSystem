# weather/data_processor.py

from .models import Weather, DailySummary
from .database import db
from flask import current_app
from datetime import datetime, date
import logging

logger = logging.getLogger(__name__)

def convert_temp(kelvin):
    TEMP_UNIT = current_app.config['TEMP_UNIT']
    if TEMP_UNIT == 'Celsius':
        return kelvin - 273.15
    elif TEMP_UNIT == 'Fahrenheit':
        return (kelvin - 273.15) * 9/5 + 32
    return kelvin

def process_daily_summary():
    CITIES = current_app.config['CITIES']
    today = date.today()
    start_of_day = datetime.combine(today, datetime.min.time())
    end_of_day = datetime.combine(today, datetime.max.time())
    start_timestamp = int(start_of_day.timestamp())
    end_timestamp = int(end_of_day.timestamp())
    for city in CITIES:
        records = Weather.query.filter(
            Weather.city == city,
            Weather.dt >= start_timestamp,
            Weather.dt <= end_timestamp
        ).all()
        if not records:
            logger.info(f"No weather records found for {city} on {today.strftime('%Y-%m-%d')}")
            continue
        temps = [convert_temp(r.temp) for r in records]
        conditions = [r.main for r in records]
        avg_temp = sum(temps) / len(temps)
        max_temp = max(temps)
        min_temp = min(temps)
        dominant_condition = max(set(conditions), key=conditions.count)
        logger.info(f"Processing summary for {city}: Avg Temp={avg_temp}")
        summary = DailySummary(
            city=city,
            date=today.strftime('%Y-%m-%d'),
            avg_temp=avg_temp,
            max_temp=max_temp,
            min_temp=min_temp,
            dominant_condition=dominant_condition
        )
        db.session.add(summary)
    db.session.commit()
    logger.info("Daily summaries processed.")
