# django-dev-superuser

[![CI](https://github.com/jerinpetergeorge/django-dev-superuser/actions/workflows/ci.yml/badge.svg)](https://github.com/jerinpetergeorge/django-dev-superuser/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/jerinpetergeorge/django-dev-superuser/branch/main/graph/badge.svg)](https://codecov.io/gh/jerinpetergeorge/django-dev-superuser)

Management commands for creating a Django superuser with ease — designed for local/dev environments.

## Installation

```bash
pip install django-dev-superuser
```

## Usage

1. Add `django_su` to your `INSTALLED_APPS`:

    ```python
    INSTALLED_APPS = [
        ...
        "django_su",
    ]
    ```

2. Run the command to create a superuser:

    ```bash
    python manage.py create_dev_su
    ```

The command is **idempotent** — if a user with the configured username already exists, it skips creation and prints a warning.

## Settings

Override defaults via `DJANGO_SU_CONFIG` in your Django settings:

```python
DJANGO_SU_CONFIG = {
    "USERNAME": "admin",       # default: "admin"
    "PASSWORD": "admin",       # default: "admin"
    "EXTRA_ARGS": {},          # extra kwargs passed to create_superuser()
}
```

## Commands

| Command | Description |
|---|---|
| `create_dev_su` | Create a superuser using the configured credentials |
| `util_restore` | Reset DB → migrate → create superuser (requires `django-extensions`) |

---

## Local Development Setup

### 1. Clone the repository

```bash
git clone https://github.com/jerinpetergeorge/django-dev-superuser.git
cd django-dev-superuser
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate       # macOS/Linux
# .venv\Scripts\activate        # Windows
```

### 3. Install development dependencies

```bash
pip install -e ".[dev]"
```

### 4. Install pre-commit hooks

```bash
pre-commit install
```

### 5. Run the tests

```bash
pytest tests/
```

### 6. Run the full tox matrix (optional)

```bash
pip install tox
tox
```

This runs tests across all supported Python (3.8–3.14) and Django (4.2–6.0) combinations.

### Code style

```bash
black src/ tests/     # auto-format
isort src/ tests/     # sort imports
flake8                # lint
```

Pre-commit hooks handle formatting automatically on each commit.
