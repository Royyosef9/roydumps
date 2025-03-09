from django.contrib.auth.models import Group, Permission

def setup_roles():
    # יצירת קבוצה למנהלים
    admin_group, created = Group.objects.get_or_create(name='Admin')
    admin_group.permissions.set(Permission.objects.all())  # למנהלים יש את כל ההרשאות
    admin_group.save()

    # יצירת קבוצה למשתמשים רגילים
    user_group, created = Group.objects.get_or_create(name='User')
    user_group.save()

    print("Roles created successfully!")
