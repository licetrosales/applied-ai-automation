import os
from urllib.parse import quote

import requests
from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-change-in-production")

WEATHER_API_BASE = "https://api.weatherapi.com/v1/current.json"


def get_api_key() -> str | None:
    return os.getenv("WEATHER_API_KEY")


def fetch_current_weather(city: str) -> tuple[dict | None, str | None]:
    """Return (weather_payload, error_message)."""
    api_key = get_api_key()
    if not api_key:
        return None, "WEATHER_API_KEY is not set. Add it to your .env file."

    city = city.strip()
    if not city:
        return None, "Please enter a city name."

    try:
        response = requests.get(
            WEATHER_API_BASE,
            params={"key": api_key, "q": city, "aqi": "no"},
            timeout=10,
        )
    except requests.RequestException:
        return None, "Could not reach WeatherAPI. Check your connection and try again."

    if response.status_code == 401:
        return None, "Invalid API key. Check WEATHER_API_KEY in your .env file."
    if response.status_code == 400:
        return None, "Location not found. Try another city name."
    if not response.ok:
        return None, f"Weather service error (HTTP {response.status_code})."

    return response.json(), None


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/weather")
def weather_lookup():
    city = request.args.get("city", "").strip()
    if not city:
        flash("Enter a city to look up weather.", "warning")
        return redirect(url_for("home"))

    data, error = fetch_current_weather(city)
    if error:
        flash(error, "error")
        return redirect(url_for("home", city=quote(city)))

    location = data["location"]
    current = data["current"]
    condition = current["condition"]

    return render_template(
        "weather.html",
        city_query=city,
        location=location,
        current=current,
        condition=condition,
    )


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
