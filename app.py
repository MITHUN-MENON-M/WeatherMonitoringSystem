# app.py

from flask import Flask, render_template
from weather.scheduler import start_scheduler, job
from weather.database import db
from weather.models import Weather, DailySummary, Alert
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)

with app.app_context():
    db.create_all()
    job(app)  # Run the job once at startup

start_scheduler(app)

@app.route('/')
def index():
    summaries = DailySummary.query.order_by(DailySummary.date.desc()).all()
    return render_template('index.html', summaries=summaries)

@app.route('/alerts')
def alerts():
    alerts = Alert.query.order_by(Alert.timestamp.desc()).all()
    return render_template('alerts.html', alerts=alerts)

@app.route('/trends')
def trends():
    return render_template('trends.html')

if __name__ == '__main__':
    app.run(debug=True)
