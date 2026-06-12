# Weather App Troubleshooting Guide

## Could Not Find requirements.txt

### Problem

```text
Could not open requirements file
```

### Cause

The terminal was opened in the wrong directory.

### Resolution

Move into the Flask project directory:

```bash
cd projects/weather-app
```

Then install dependencies:

```bash
pip install -r requirements.txt
```

### Verification

```bash
pwd
```

Should display the weather-app directory and the installation should complete successfully.

---

## Cursor File Explorer Hidden

### Problem

Project files were not visible in the Cursor sidebar.

### Cause

The Explorer panel was accidentally closed or hidden.

### Resolution

Open the Explorer:

```text
CMD + SHIFT + E
```

### Verification

Project files appear in the left sidebar.

---

## Git Commands Showed No Changes

### Problem

Git did not detect any modified files.

### Cause

Changes had already been committed.

### Resolution

Check repository status:

```bash
git status
```

### Verification

Expected output:

```text
nothing to commit, working tree clean
```

---

## Flask App Showed HTTP 403

### Problem

Browser displayed:

```text
Access to 127.0.0.1 was denied
HTTP ERROR 403
```

### Cause

Possible causes:

* Flask application was not started correctly
* Browser cache interference
* Browser extension interference

### Resolution

Navigate to the project:

```bash
cd projects/weather-app
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Start Flask:

```bash
python3 app.py
```

If necessary:

* Open an Incognito window
* Hard refresh the page

```text
CMD + SHIFT + R
```

### Verification

Terminal displays:

```text
Running on http://127.0.0.1:5000
```

Browser loads:

```text
http://127.0.0.1:5000
```

---

## app.py Showed Command Not Found

### Problem

```text
zsh: command not found: app.py
```

### Cause

The script was executed directly instead of through Python.

### Resolution

Incorrect:

```bash
app.py
```

Correct:

```bash
python3 app.py
```

### Verification

The Flask application starts successfully.

---

## Flask Dependencies Missing

### Problem

```text
ModuleNotFoundError: No module named 'requests'
```

### Cause

Dependencies were not installed in the active virtual environment.

### Resolution

Install project dependencies:

```bash
pip install -r requirements.txt
```

### Verification

Application starts without import errors.

---

## Git Merge Opened Vim Editor

### Problem

After running:

```bash
git merge improve-ui
```

Git opened Vim and the terminal appeared frozen.

### Cause

Git was waiting for confirmation of the merge commit message.

### Resolution

Exit Vim and complete the merge:

1. Press:

```text
Esc
```

2. Type:

```text
:wq
```

3. Press:

```text
Enter
```

### Verification

Run:

```bash
git status
```

Expected output:

```text
On branch main
nothing to commit, working tree clean
```

Then push:

```bash
git push origin main
```

---
