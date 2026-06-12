# Weather Dashboard Local Development Runbook

## Purpose

This runbook documents the procedure for setting up, running, and validating the Weather Dashboard project in a local development environment.

---

## Project Location

```text
projects/weather-app/
```

---

## Prerequisites

### Software

* Python 3
* Cursor IDE
* Git

### External Service

* WeatherAPI account
* WeatherAPI key

---

## Project Structure

```text
weather-app/
├── app.py
├── requirements.txt
├── .env.example
├── README.md
├── templates/
│   ├── base.html
│   ├── index.html
│   └── weather.html
└── static/css/
    └── style.css
```

---

## Initial Project Generation

The project was initially generated using Cursor AI.

### Initial Prompt

```text
Create a Flask weather dashboard using WeatherAPI.com.

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

---

## Local Setup Procedure

### Navigate to Project

```bash
cd projects/weather-app
```

### Create Virtual Environment

```bash
python3 -m venv venv
```

### Activate Virtual Environment

```bash
source venv/bin/activate
```

Expected prompt:

```text
(venv)
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
WEATHER_API_KEY=your_api_key_here
```

### Important

* Never commit `.env` files to GitHub.
* Store API keys only in local environment files.

---

## Start Application

Run:

```bash
python app.py
```

Expected output:

```text
Running on http://127.0.0.1:5000
```

---

## Functional Verification

Open:

```text
http://127.0.0.1:5000
```

Verify:

* Application loads successfully.
* Search form is visible.
* City search works.
* Weather data is displayed.
* WeatherAPI requests succeed.

---

## Frontend Improvement Iteration

A second Cursor AI prompt was used to improve the user interface.

### Frontend Improvement Prompt

```text
I want to improve the UI of this Flask weather app step by step as a learning exercise.

Please improve only:

- templates/index.html
- static/css/style.css

Goals:

- modern weather dashboard appearance
- blue and gold accents
- improved typography and spacing
- subtle hover animations
- better responsive layout
- weather-related visual feeling

Requirements:

- keep the Flask backend unchanged
- explain every change before editing
- make incremental improvements
- avoid rewriting the whole project
- suggest a git commit message afterward
```

### Improvements Introduced

* Improved typography
* Improved spacing
* Responsive layout
* Blue and gold color palette
* Hover animations
* Better visual hierarchy
* Improved CSS organization

---

## Stop Application

Press:

```text
CTRL + C
```

---

## Deactivate Virtual Environment

When finished:

```bash
deactivate
```

---

## Operational Notes

### Development Environment

| Component   | Version                   |
| ----------- | ------------------------- |
| Cursor      | 3.5.17                    |
| VSCode Base | 1.105.1                   |
| Build Type  | Stable                    |
| Layout      | Glass                     |
| OS          | macOS Darwin arm64 25.5.0 |

### Cursor Configuration

* Cursor Mode: Auto
* Default Auto Model
* Cursor Agent enabled

---

## Related Documentation

### Implementation

```text
docs/implementation-notes/weather-dashboard-ai-development.md
```

### Learning Notes

```text
docs/learning-notes/ai-assisted-development-notes.md
```

### Troubleshooting

```text
docs/troubleshooting/weather-app-common-issues.md
```

### Project Source

```text
projects/weather-app/
```
