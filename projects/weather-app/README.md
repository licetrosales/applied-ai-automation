# Weather Dashboard (Flask + WeatherAPI.com)

A small Flask app that shows current weather for any city using the [WeatherAPI current weather endpoint](https://www.weatherapi.com/docs/).

## Prerequisites

- Python 3.10+
- A free API key from [weatherapi.com](https://www.weatherapi.com/signup.aspx)

## Setup

From the project directory:

```bash
cd projects/weather-app
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set your key:

```env
WEATHER_API_KEY=your_actual_api_key
```

## Run locally

```bash
source venv/bin/activate
python app.py
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

- **Home** (`/`) — search form
- **Weather lookup** (`/weather?city=London`) — current conditions for the city

## Environment variables

| Variable | Required | Description |
|----------|----------|-------------|
| `WEATHER_API_KEY` | Yes | WeatherAPI.com API key |
| `FLASK_SECRET_KEY` | No | Secret for flash messages (defaults to a dev value) |

## Project layout

```text
weather-app/
├── app.py
├── requirements.txt
├── .env.example
├── templates/
│   ├── base.html
│   ├── index.html
│   └── weather.html
└── static/css/
    └── style.css
```
