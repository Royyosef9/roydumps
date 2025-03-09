import os
import secrets
import logging.config
from pathlib import Path
from dotenv import load_dotenv
from django.core.cache import cache
from django.contrib.auth.models import User

# טוען את משתני הסביבה מקובץ .env
load_dotenv()

# נתיב בסיסי של הפרויקט
BASE_DIR = Path(__file__).resolve().parent.parent

# הגדרות לוגים
from backend.config.logging import LOGGING_CONFIG
LOGGING = LOGGING_CONFIG

# אפליקציות מותקנות
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'django_prometheus',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'backend.middleware.RequestTimingMiddleware',
]

# SECRET_KEY – מפתח סודי מאובטח
SECRET_KEY = os.getenv("SECRET_KEY") or secrets.token_urlsafe(50)

# מצב DEBUG – רק בסביבת פיתוח
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# דומיינים מותרים
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

# הגדרת CORS
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "*").split(",")

# בסיס נתונים
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'dev_database'),
        'USER': os.getenv('DB_USER', 'royyo'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'devpassword'),
        'HOST': os.getenv('DB_HOST', 'postgres_db'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

# Redis – קאש
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# שימוש בקאש (דוגמה)
def get_users():
    users = cache.get("users")
    if not users:
        users = list(User.objects.all().values())
        cache.set("users", users, timeout=300)
    return users

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]