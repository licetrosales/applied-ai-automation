# Cursor + Flask Weather Dashboard Setup (macOS)

## Goal

Explore AI-assisted software development using Cursor AI and Flask.

## Tools Used

- Cursor IDE
- Python 3
- Flask
- [WeatherAPI.com](http://WeatherAPI.com)
- Git + GitHub
- macOS

## Cursor Configuration

- Cursor mode: Auto
- AI model: default Auto model
- Cursor Agent used for code generation

## Initial Prompt

```text

Create a Flask weather dashboard using [WeatherAPI.com](http://WeatherAPI.com).

Requirements:

- Use Python and Flask

- Create routes for home and weather lookup

- Use environment variables for API keys

- Read WEATHER_API_KEY from a .env file

- Include requirements.txt

- Include .env.example

- Include templates and CSS

- Create a modern responsive UI

- Allow users to search by city

- Explain how to run locally

Use WeatherAPI current weather endpoint.

Provide all related files.

```

## Generated Project Structure

```text

projects/weather-app/

├── [app.py](http://app.py)
├── requirements.txt
├── .env.example
├── [README.md](http://README.md)
├── templates/
│   ├── base.html
│   ├── index.html
│   └── weather.html
└── static/css/
    └── style.css

```

## Setup Steps

### Create virtual environment

```bash

python3 -m venv venv

```

### Activate environment

```bash

source venv/bin/activate

```

### Install dependencies

```bash

pip install -r requirements.txt

```

### Configure API key

Create `.env`:

```env

WEATHER_API_KEY=your_api_key_here

```

### Run application

```bash

python [app.py](http://app.py)

```

### Open in browser

```text

[http://127.0.0.1:5000](http://127.0.0.1:5000)

```

## Observations

- Cursor generated backend and frontend automatically
- Flask routes connected templates and API calls
- HTML templates used Jinja syntax
- CSS styling created a modern UI automatically
- Git workflow integrated well with Cursor

