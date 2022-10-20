from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    code의 snippet의 owner만 수정할 수 있게 하는 Custom permission 임.
    """

    def has_object_permission(self, request, view, obj):
        # 읽기 권한 = 어떤 요청이든 허용
        # 따라서 get, head, option 요청은 항상 허용
        if request.method in permissions.SAFE_METHODS:
            return True

        # 쓰기 권한은 snippet의 오너만.
        return obj.owner == request.user
