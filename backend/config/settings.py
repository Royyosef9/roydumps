import os
from pathlib import Path
from django.core.cache import cache

# הגדרות בסיסיות
BASE_DIR = Path(__file__).resolve().parent.parent

# ייבוא לוגים
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
    'rest_framework',  # Django REST Framework
    'corsheaders',  # CORS Middleware
    'django_prometheus',  # ניטור עם Prometheus
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.authentication.SessionAuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # תמיכה ב-CORS
]

# הוספת ה-Middleware לניטור תעבורה
MIDDLEWARE.append("backend.middleware.RequestTimingMiddleware")

# הגדרות בסיס נתונים (PostgreSQL)
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

# הגדרת Caching עם Redis
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# שימוש ב-Redis Cache בקוד
def get_users():
    users = cache.get("users")
    if not users:
        users = list(User.objects.all().values())
        cache.set("users", users, timeout=300)  # שמירת הנתונים ל-5 דקות
    return users

# קבצים סטטיים
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# אבטחה
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '*').split(',')
