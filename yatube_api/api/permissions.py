from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Пользовательское разрешение для проверки авторства объекта.

    Разрешает доступ к объекту только для чтения (GET, HEAD, OPTIONS)
    пользователям, которые не являются автором объекта.
    Для всех остальных методов (создание, обновление, удаление)
    требует, чтобы пользователь был автором объекта.
    """

    def has_object_permission(self, request, view, obj):
        return (
            (request.method in permissions.SAFE_METHODS)
            or (obj.author == request.user)
        )
