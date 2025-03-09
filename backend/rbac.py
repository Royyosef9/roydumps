from functools import wraps
from django.http import JsonResponse
from django.contrib.auth.models import Group, Permission

def setup_roles():
    """
    יוצר קבוצות של משתמשים ומחלק הרשאות בהתאם (Admin ו-User)
    """
    admin_group, _ = Group.objects.get_or_create(name='Admin')
    admin_group.permissions.set(Permission.objects.all())
    admin_group.save()

    user_group, _ = Group.objects.get_or_create(name='User')
    user_group.save()

    print("✅ Roles setup completed")

def require_permission(perm_name):
    """
    דקורטור לבדיקת הרשאה לפני ביצוע פעולה
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.has_perm(perm_name):
                return JsonResponse({'error': 'Permission denied'}, status=403)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator