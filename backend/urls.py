from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Health Check Endpoint
def health_check(request):
    return JsonResponse({"status": "ok"}, status=200)

urlpatterns = [
    path('admin/', admin.site.urls),  # דף ניהול של Django
    path('api/', include('backend.api.urls')),  # הוספת ה-API אם קיים
    path('health/', health_check, name="health_check"),  # בדיקת זמינות השרת
]
