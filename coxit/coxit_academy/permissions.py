from rest_framework import permissions

class IsMentorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        
        if obj.mentor:
            return obj.mentor.linked_user == request.user
        
        return False
        