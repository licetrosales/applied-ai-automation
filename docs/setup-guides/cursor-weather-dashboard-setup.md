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

### Cursor Version Information

| Component | Version |
|---|---|
| Cursor | 3.5.17 |
| VSCode Base | 1.105.1 |
| Build Type | Stable |
| Layout | glass |
| OS | macOS Darwin arm64 25.5.0 |

### Workflow Notes

The newer Cursor "glass" layout was used for the implementation. It differs form the classic version in some UI elements such as:
- terminal access
- repository explorer
- Git panels

were less immediately visible compared to traditional VSCode layouts.

Because of this, several workflows were performed directly through the integrated terminal instead of GUI buttons.

### Important Discovery

The repository explorer was opened using:

```text
CMD + SHIFT + E
```

This shortcut became essential for navigating project structure in the glass layout UI.

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
## Additional Workflow Notes

### Reopening Existing Flask Project

When reopening the project after some time, the following steps were required:

### Navigate to project directory

```bash
cd ~/Documents/GitHub/applied-ai-automation/projects/weather-app
```

### Activate existing virtual environment

```bash
source venv/bin/activate
```

### Reinstall dependencies (if required)

```bash
pip install -r requirements.txt
```

Observation:

* dependencies may need reinstalling after Python updates or environment changes
* `ModuleNotFoundError` indicated missing packages inside the virtual environment

### Run Flask application

```bash
python app.py
```

Expected terminal output:

```text
Running on http://127.0.0.1:5000
```

### Browser Access Observation

The application initially returned:

```text
HTTP ERROR 403
```

Resolution:

* Flask server was running correctly
* opening the URL in a private/incognito browser window resolved the issue

---

## Git Workflow Used For UI Improvements

### Synchronize local repository

```bash
git fetch --all
git pull
```

Observation:

* `git fetch --all` updates remote branch information locally
* `git pull` merges latest changes into the current branch

### Create feature branch

```bash
git checkout -b improve-ui
```

Observation:

* UI changes were isolated from the `main` branch
* feature branch workflow reduced risk during experimentation

---

## AI-Assisted UI Improvement Prompt

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

---
## UI Improvements Introduced

Cursor AI generated improvements including:

- refined typography and spacing
- blue/gold design palette
- weather-themed visual atmosphere
- responsive hero layout
- hover animations and micro-interactions
- enhanced CSS variable organization

## Key Technical Learnings
- virtual environments are essential for Python dependency isolation
- pip install -r requirements.txt is often required after environment recreation
- Git feature branches reduce risk during experimentation
- reviewing AI-generated diffs improves learning and code comprehension
- structured prompts significantly improve AI output quality
- Cursor Auto mode accelerates frontend iteration workflows


