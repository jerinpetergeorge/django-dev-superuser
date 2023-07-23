SECRET_KEY = "NOT_A_SECRET"

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django_su",
]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3"}}

TEMPLATES = [{"BACKEND": "django.template.backends.django.DjangoTemplates"}]

MIDDLEWARE = []

USE_TZ = True
