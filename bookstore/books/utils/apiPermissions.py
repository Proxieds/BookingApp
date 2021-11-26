from rest_framework import permissions

class APIPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        api_key = "hK0iP5dL7bW3fP3y"
        request_key = request.query_params.get('apikey', False)
        if api_key == request_key:
            return True
        return False