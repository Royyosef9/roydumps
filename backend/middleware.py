import time
import logging

logger = logging.getLogger(__name__)

class RequestTimingMiddleware:
    """
    Middleware לניטור ביצועים – מודד כמה זמן לוקחת כל בקשה ומוסיף לוגים.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()  # תחילת מדידת הזמן
        response = self.get_response(request)  # המשך הבקשה
        duration = time.time() - start_time  # חישוב משך הבקשה

        # רישום לוגים על משך הבקשה
        logger.info(f"⏳ {request.method} {request.path} לקח {duration:.3f} שניות")

        # הוספת מידע לכותרות ה-Response (לניטור)
        response["X-Request-Duration"] = f"{duration:.3f}s"
        return response