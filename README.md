# Real-Time Weather Monitoring System

## Description

A real-time data processing system to monitor weather conditions and provide summarized insights using rollups and aggregates, with a beautiful web UI. The system fetches weather data from the OpenWeatherMap API for major Indian metros and displays daily summaries, alerts, and historical trends.

## Features

- **Real-time Data Fetching**: Retrieves weather data at configurable intervals.
- **Data Processing**: Converts temperatures, calculates daily summaries, and determines dominant weather conditions.
- **Alerts System**: Triggers alerts based on user-defined thresholds.
- **Web UI**: Displays daily summaries, alerts, and temperature trends.
- **Visualizations**: Generates and displays historical temperature trends.

## Project Structure

```
WeatherMonitoringSystem/
├── app.py
├── config.py
├── requirements.txt
├── static/
│   ├── style.css
│   └── trends.png
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── alerts.html
│   └── trends.html
├── weather/
│   ├── __init__.py
│   ├── alert_system.py
│   ├── data_processor.py
│   ├── database.py
│   ├── models.py
│   ├── scheduler.py
│   ├── visualization.py
│   └── weather_fetcher.py
└── README.md
```

- **app.py**: Main application file to run the Flask web server.
- **config.py**: Configuration settings for the application.
- **requirements.txt**: Python package dependencies.
- **templates/**: HTML templates for the web UI.
- **static/**: Static files like CSS and images.
- **weather/**: Python modules for data fetching, processing, alerts, and scheduling.

## Setup Instructions

### Prerequisites

- **Python 3.8 or higher**
- **pip** package installer

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/MITHUN-MENON-M/WeatherMonitoringSystem.git
   cd WeatherMonitoringSystem
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```
**I HAVE KEPT MY API KEY, YOU CAN USE CHANGE IF YOU WANT **

5. **Run the Application**

   ```bash
   python app.py
   ```

6. **Access the Web Interface**

   - Open your web browser and navigate to `http://localhost:5000` to view the application.

## Usage Instructions

- **Daily Summaries**

  - View the average, maximum, and minimum temperatures for each city.
  - See the dominant weather condition for the day.

- **Alerts**

  - Check for any triggered alerts based on the configured temperature thresholds.

- **Trends**

  - View historical temperature trends plotted over time.

## Design Choices

- **Flask**: Chosen for creating the web application due to its simplicity and flexibility.
- **SQLite**: Used as the database because it's lightweight and doesn't require additional setup.
- **SQLAlchemy**: Utilized as the ORM for database operations.
- **APScheduler**: Employed for scheduling periodic tasks within the Flask application context.
- **Matplotlib and Pandas**: Used for data visualization and manipulation.

## Dependencies

Install all dependencies using:

```bash
pip install -r requirements.txt
```

- **Flask**
- **Flask_SQLAlchemy**
- **requests**
- **APScheduler**
- **matplotlib**
- **pandas**

## File Overview

### app.py

Main application file that initializes the Flask app, database, and starts the scheduler.

### config.py

Contains configuration variables such as API keys, city list, thresholds, and database URI.

### requirements.txt

List of all Python packages required to run the application.

### weather/

Contains all backend logic for fetching data, processing, alerts, scheduling, and visualization.

- **weather_fetcher.py**: Fetches weather data from OpenWeatherMap API.
- **data_processor.py**: Processes data and calculates daily summaries.
- **alert_system.py**: Checks for alert conditions and records alerts.
- **scheduler.py**: Schedules periodic tasks.
- **visualization.py**: Generates temperature trends graph.
- **models.py**: Database models for SQLAlchemy.
- **database.py**: Initializes the database connection.

### templates/

Contains HTML templates for rendering the web pages.

- **base.html**: Base template that other templates extend.
- **index.html**: Displays daily weather summaries.
- **alerts.html**: Shows triggered alerts.
- **trends.html**: Displays the trends graph.

### static/

Contains static files like CSS and images.

- **style.css**: Stylesheet for the web application.
- **trends.png**: Generated trends graph image.

## Troubleshooting

- **No Data Displayed**

  - Ensure that the application has run for at least one interval to fetch and process data.
  - Check the terminal for any error messages.
  - Verify that your API key is correct and has not exceeded the rate limit.

- **API Errors**

  - If you receive errors related to the API, double-check your API key in `config.py`.
  - Ensure you have internet connectivity.

- **Dependencies Issues**

  - If you encounter module not found errors, ensure all dependencies are installed using the provided `requirements.txt`.

- **Database Issues**

  - If you suspect issues with the database, you can delete the `weather_data.db` file and restart the application to recreate it.

## Notes

- The application fetches data at intervals defined by `INTERVAL_MINUTES`. Adjust this value in `config.py` if needed.
- Be mindful of OpenWeatherMap's API rate limits to avoid being blocked.
- The application runs indefinitely. Use `CTRL + C` in the terminal to stop it.

