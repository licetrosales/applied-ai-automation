# AI-Assisted Development Learning Notes

## Concepts Learned

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

Sensitive data like API keys should be stored in `.env`.

`.env` should never be committed to GitHub.

### Git Status Symbols

- `A` = Added file
- `M` = Modified file
- `U` = Untracked file

### Git Workflow Used

Stage files:

```bash
git add .
```

Check repository status:

```bash
git status
```

Commit changes:

```bash
git commit -m "message"
```

Push to GitHub:

```bash
git push
```

### Virtual Environment

`venv` isolates Python dependencies per project.

### AI Workflow Observation

Cursor can:
- generate full-stack applications
- create file structures
- generate documentation
- scaffold Flask apps quickly

Human responsibilities still include:
- understanding architecture
- validating code
- debugging
- documenting
- committing changes properly

## Reflection

This exercise demonstrated how AI can accelerate software development lifecycle tasks:
- scaffolding
- UI generation
- boilerplate setup
- API integration
- documentation

However, understanding concepts remains essential.
