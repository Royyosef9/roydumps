from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from backend.healthcheck import health_check

# בדיקת זמינות בסיסית – עבור Load Balancer
def simple_health_check(request):
    return JsonResponse({"status": "ok"}, status=200)

urlpatterns = [
    path("admin/", admin.site.urls),  # Django Admin
    path("api/", include("backend.api.urls")),  # API ראשי
    path("healthz/", health_check, name="health_check"),  # בדיקה מתקדמת
    path("health/", simple_health_check, name="simple_health_check"),  # בדיקה בסיסית
]
# Compare this snippet from backend/api/urls.py: