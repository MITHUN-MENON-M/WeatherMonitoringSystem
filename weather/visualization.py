# weather/visualization.py

from .models import DailySummary
from .database import db
from flask import current_app
import matplotlib.pyplot as plt
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def generate_trends():
    data = []
    CITIES = current_app.config['CITIES']
    for city in CITIES:
        summaries = DailySummary.query.filter_by(city=city).all()
        for summary in summaries:
            data.append({
                'City': summary.city,
                'Date': summary.date,
                'AvgTemp': summary.avg_temp
            })
    df = pd.DataFrame(data)
    if df.empty:
        logger.info("No data available for generating trends.")
        return

    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Aggregate data to ensure unique Date-City combinations
    df = df.groupby(['Date', 'City'], as_index=False).mean()

    pivot_df = df.pivot(index='Date', columns='City', values='AvgTemp')

    # Plotting
    plt.figure(figsize=(10, 6))
    pivot_df.plot(ax=plt.gca())
    plt.xlabel('Date')
    plt.ylabel('Average Temperature')
    plt.title('Daily Average Temperature Trends')
    plt.legend()
    plt.tight_layout()
    plt.savefig('static/trends.png')
    plt.close()
    logger.info("Temperature trends graph generated.")
