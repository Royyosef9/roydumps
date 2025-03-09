import os
import logging
import time
import redis
from django.http import JsonResponse
from django.db import connection
from django.core.cache import cache

logger = logging.getLogger(__name__)
START_TIME = time.time()

def check_database():
    """ בדיקה אם PostgreSQL מגיב """
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return True
    except Exception as e:
        logger.error(f"❌ Database Health Check Failed: {e}")
        return False

def check_redis():
    """ בדיקה אם Redis מגיב """
    try:
        cache.set("healthcheck", "ok", timeout=5)
        return cache.get("healthcheck") == "ok"
    except (redis.exceptions.ConnectionError, redis.exceptions.TimeoutError) as e:
        logger.error(f"❌ Redis Health Check Failed: {e}")
        return False

def health_check(request):
    """ API שמחזיר סטטוס כולל של השרת (DB, Redis, Django) """
    db_status = check_database()
    redis_status = check_redis()
    uptime_seconds = int(time.time() - START_TIME)

    overall = "healthy" if db_status and redis_status else "unhealthy"
    status_code = 200 if overall == "healthy" else 500

    return JsonResponse({
        "status": overall,
        "uptime": f"{uptime_seconds} seconds",
        "checks": {
            "django_running": True,
            "database": db_status,
            "redis": redis_status
        }
    }, status=status_code)