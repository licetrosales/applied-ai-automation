# Cursor + Flask Weather Dashboard (macOS)

## Goal

Build and run a Flask-based weather dashboard using Cursor AI, Python, and WeatherAPI.

## Tools Used

- Cursor IDE
- Python 3
- Flask
- WeatherAPI
- Git
- GitHub
- macOS

## Development Environment

| Component | Version |
|------------|------------|
| Cursor | 3.5.17 |
| VSCode Base | 1.105.1 |
| Build Type | Stable |
| Layout | Glass |
| OS | macOS Darwin arm64 25.5.0 |

## Cursor Configuration

- Cursor Mode: Auto
- AI Model: Default Auto Model
- Cursor Agent used for code generation and project scaffolding

The project was developed using Cursor's Glass layout. Several development tasks were performed through the integrated terminal.

## Initial AI Prompt

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

## Project Structure

```text
projects/weather-app/

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

## Installation

### Create Virtual Environment

```bash
python3 -m venv venv
```

### Activate Environment

Activate the virtual environment before installing dependencies or running the application.

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

### Configure API Key

Create a `.env` file:

```env
WEATHER_API_KEY=your_api_key_here
```

## Verification

### Run Application

Start the Flask development server from the project root directory.

```bash
python app.py
```

Expected output:

```text
Running on http://127.0.0.1:5000
```
### Stop Application

Stop the Flask development server:

```text
CTRL + C
```
### Deactivate Environment

Exit the virtual environment when development work is finished:

```bash
deactivate
```

### Open in Browser

```text
http://127.0.0.1:5000
```

Verify that:

- The Flask application loads successfully.
- Weather data can be retrieved for a city search.
- The WeatherAPI integration returns current weather information.

## AI-Assisted Frontend Improvements

### UI Improvement Prompt

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

Cursor AI generated frontend enhancements including:

- Improved typography and spacing
- Blue and gold visual theme
- Responsive dashboard layout
- Hover animations and micro-interactions
- Improved visual hierarchy
- Better CSS organization and maintainability

## Key Learnings

- Virtual environments isolate project dependencies and improve reproducibility.
- Environment variables protect sensitive configuration such as API keys.
- Flask provides a lightweight framework for API-driven web applications.
- Well-structured prompts improve AI-generated code quality.
- Cursor AI accelerates scaffolding, UI iteration, and documentation generation.
- Human validation remains essential for architecture, debugging, and maintenance.
