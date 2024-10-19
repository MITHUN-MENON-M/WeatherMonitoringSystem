# weather/alert_system.py

from .models import Weather, Alert
from .database import db
from flask import current_app
from .data_processor import convert_temp
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def check_alerts():
    CITIES = current_app.config['CITIES']
    TEMP_THRESHOLD = current_app.config['TEMP_THRESHOLD']
    CONSECUTIVE_ALERTS = current_app.config['CONSECUTIVE_ALERTS']
    for city in CITIES:
        records = Weather.query.filter_by(city=city).order_by(Weather.dt.desc()).limit(CONSECUTIVE_ALERTS).all()
        if len(records) < CONSECUTIVE_ALERTS:
            continue
        temps = [convert_temp(r.temp) for r in records]
        if all(t > TEMP_THRESHOLD for t in temps):
            timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
            message = f'Temperature in {city} has exceeded {TEMP_THRESHOLD} degrees for {CONSECUTIVE_ALERTS} consecutive updates.'
            alert = Alert(city=city, temp=temps[0], timestamp=timestamp, message=message)
            db.session.add(alert)
            logger.info(f"Alert triggered for {city}: {message}")
    db.session.commit()
