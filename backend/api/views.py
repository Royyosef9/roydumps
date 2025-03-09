from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from backend.rbac import require_permission  # יבוא של מערכת ההרשאות שלנו

@api_view(["GET", "POST"])
@permission_classes([permissions.IsAuthenticated])  # רק משתמשים מחוברים יכולים לגשת
def user_list(request):
    """ 📌 מציג רשימת משתמשים (GET) או יוצר משתמש חדש (POST) """
    if request.method == "GET":
        users = User.objects.all().values("id", "username")
        return Response({"users": list(users)}, status=status.HTTP_200_OK)

    elif request.method == "POST":
        if "username" not in request.data or not request.data["username"].strip():
            return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)

        @require_permission("edit_users")  # רק אדמינים יכולים להוסיף משתמשים
        def create_user():
            user = User.objects.create(username=request.data["username"])
            return Response({"id": user.id}, status=status.HTTP_201_CREATED)

        return create_user()

@api_view(["GET", "PUT", "DELETE"])
@permission_classes([permissions.IsAuthenticated])  # רק משתמשים מחוברים יכולים לגשת
def user_detail(request, pk):
    """ 📌 מנהל פעולות על משתמש ספציפי (קריאה, עריכה, מחיקה) """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        return Response({"id": user.id, "username": user.username}, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        if "username" not in request.data or not request.data["username"].strip():
            return Response({"error": "Username is required"}, status=status.HTTP_400_BAD_REQUEST)

        @require_permission("edit_users")  # רק אדמינים יכולים לעדכן משתמשים
        def update_user():
            user.username = request.data["username"]
            user.save()
            return Response({"message": "User updated"}, status=status.HTTP_200_OK)

        return update_user()

    elif request.method == "DELETE":
        @require_permission("delete_users")  # רק אדמינים יכולים למחוק משתמשים
        def delete_user():
            user.delete()
            return Response({"message": "User deleted"}, status=status.HTTP_204_NO_CONTENT)

        return delete_user()