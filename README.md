# django-dev-superuser

## Installation

        pip install django-dev-superuser

## Usage

1. Add `django_su` to your `INSTALLED_APPS` setting like this:

        INSTALLED_APPS = [
            ...
            'django_su',
        ]
2. Run `python manage.py create_dev_su` to create a superuser

## Settings

* `DJANGO_SU_USERNAME` (type: `str`) - username for the superuser (default: `admin`)
* `DJANGO_SU_PASSWORD` (type: `str`) - password for the superuser (default: `password`)
* `DJANGO_SU_EXTRA_ARGS` (type: `dict`) - extra arguments for the superuser (default: `{}`)
