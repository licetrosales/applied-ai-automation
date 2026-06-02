## Could not find requirements.txt

### Problem

```text

Could not open requirements file

```

### Cause

Terminal was opened in the wrong directory.

### Fix

Move into the Flask project folder first:

```bash

cd projects/weather-app

```

Then run:

```bash

pip install -r requirements.txt

```

---

## Cursor file explorer hidden

### Problem

Project files were not visible in the Cursor sidebar.

### Fix

Open Explorer with:

```text

CMD + SHIFT + E

```

---

## Git commands showed no changes

### Cause

Files were already committed previously.

### Verification

Use:

```bash

git status

```

If output shows:

```text

nothing to commit

```

then repository is already clean.

---

---

## Flask app showed HTTP 403 in browser

### Problem

Browser displayed:

```text

Access to 127.0.0.1 was denied

HTTP ERROR 403

```

even though Flask server was running.

### Cause

The Flask application was not started correctly before opening the browser.

In another case, browser cache or extensions interfered with localhost access.

### Fix

Run Flask from inside the correct project directory:

```bash

cd ~/Documents/...../projects/weather-app

```

Activate virtual environment:

```bash

source venv/bin/activate

```

Run Flask application:

```bash

python3 app.py

```

Verify terminal shows:

```text

Running on http://127.0.0.1:5000

```

Then open:

```text

http://127.0.0.1:5000

```

If browser still shows 403:

* open in Incognito mode
* or hard refresh with:

```text

CMD + SHIFT + R

```

---

## app.py showed command not found

### Problem

```text

zsh: command not found: app.py

```

### Cause

`app.py` was executed directly instead of through Python.

### Fix

Wrong:

```bash

app.py

```

Correct:

```bash

python3 app.py

```

---

## Flask dependencies missing

### Problem

```text

ModuleNotFoundError: No module named 'requests'

```

### Cause

Dependencies were not installed inside the current virtual environment.

### Fix

Install dependencies from `requirements.txt`:

```bash

pip install -r requirements.txt

```

