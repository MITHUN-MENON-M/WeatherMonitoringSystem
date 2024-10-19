# weather/scheduler.py

from apscheduler.schedulers.background import BackgroundScheduler
from .weather_fetcher import fetch_weather_data
from .data_processor import process_daily_summary
from .alert_system import check_alerts
from .visualization import generate_trends
from flask import current_app

def start_scheduler(app):
    INTERVAL_MINUTES = app.config['INTERVAL_MINUTES']
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=lambda: job(app), trigger="interval", minutes=INTERVAL_MINUTES)
    scheduler.start()

def job(app):
    with app.app_context():
        fetch_weather_data()
        process_daily_summary()
        check_alerts()
        generate_trends()
