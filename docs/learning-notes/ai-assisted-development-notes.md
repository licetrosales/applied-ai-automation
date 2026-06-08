# AI-Assisted Development Learning Notes

## Goal

Document concepts learned while building a Flask Weather Dashboard using Cursor AI.

---

## Flask Concepts Learned

### Flask Routes

Routes connect URLs to Python functions.

Example:

```python
@app.route("/")
def home():
    return render_template("index.html")
```

### Templates

Flask uses Jinja templates to generate HTML dynamically.

Example:

```html
{{ location.name }}
```

### Environment Variables

Sensitive information such as API keys should be stored in environment files.

Example:

```text
.env
```

Key lesson:

- API keys should never be committed to GitHub.
- Environment variables separate configuration from source code.

---

## Cursor Development Workflow

### Useful Cursor Shortcuts (macOS)

| Shortcut | Purpose |
|-----------|-----------|
| CMD + SHIFT + E | Open repository explorer |
| CMD + SHIFT + P | Open Command Palette |
| CTRL + ` | Open integrated terminal |
| CMD + S | Save file |
| CMD + / | Toggle comments |
| CMD + B | Toggle sidebar |
| CMD + P | Quick file search |
| CMD + SHIFT + F | Search across project |

### Most Useful Discovery

```text
CMD + SHIFT + E
```

This shortcut revealed the project file explorer in Cursor's newer interface.

---

## Virtual Environments

Python virtual environments isolate project dependencies.

Example:

```bash
python -m venv venv
```

Benefits:

- Prevents dependency conflicts
- Keeps project environments independent
- Improves reproducibility

---

## AI-Assisted Development Observations

During this project, Cursor was able to:

- Generate Flask application scaffolding
- Create project structures
- Generate HTML templates
- Produce CSS styling
- Generate documentation drafts
- Assist with API integration

### Human Responsibilities

AI accelerated development, but several tasks still required human judgment:

- Understanding application architecture
- Validating generated code
- Debugging issues
- Managing project structure
- Writing and maintaining documentation
- Reviewing AI-generated output

---

## Reflection

This project demonstrated how AI can accelerate software development by reducing boilerplate work and speeding up prototyping.

The most important lesson was that AI increases productivity, but understanding the underlying concepts remains essential for debugging, validation, and long-term maintenance.
