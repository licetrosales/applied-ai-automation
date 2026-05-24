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

| Symbol | Meaning |
|---|---|
| `U` | Untracked file (new file not yet added to Git) |
| `A` | Added/staged file |
| `M` | Modified file |

### Git States

- **Untracked** → Git has never tracked the file
- **Unstaged** → File changed but not prepared for commit
- **Staged** → Ready to commit

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
### Pulling Latest Changes From GitHub
#### Update Local Repository

If changes were pushed to GitHub and you want them on your laptop:
```bash
git pull
```
This downloads and updates your local repository with the newest remote changes.

#### Recommended Workflow

Before pulling:
```bash
git status
```
If there are uncommitted changes:

- commit them first
- or stash them

Then:
```bash
git pull
```

## Useful Cursor Shortcuts (macOS)

| Shortcut | Purpose |
|---|---|
| `CMD + SHIFT + E` | Open file explorer / repository structure |
| `CMD + SHIFT + P` | Open Command Palette |
| `CTRL + \`` | Open integrated terminal or View → Terminal|
| `CMD + S` | Save current file |
| `CMD + /` | Toggle code comments |
| `CMD + B` | Toggle sidebar visibility |
| `CMD + P` | Quick open files |
| `CMD + SHIFT + F` | Search across project |




### Most Useful During This Project

The most important shortcut discovered during setup was:

```text
CMD + SHIFT + E
```

This revealed the hidden repository file explorer in Cursor's newer "glass" layout UI.
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

### Flask Server Control
#### Start App

Inside project folder:
```bash
python app.py
```

#### Stop App

While terminal is running Flask:
```text
CTRL + C
```
This safely stops the Flask development server.

### Exit Virtual Environment

After stopping Flask:
```text
deactivate
```
This returns terminal to the normal macOS shell environment.

### Full Daily Workflow Example
```bash
cd projects/weather-app
source venv/bin/activate
git pull
python app.py
```
After work:
```text
CTRL + C
deactivate
```

## Reflection

This exercise demonstrated how AI can accelerate software development lifecycle tasks:
- scaffolding
- UI generation
- boilerplate setup
- API integration
- documentation

However, understanding concepts remains essential.
