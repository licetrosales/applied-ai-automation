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
