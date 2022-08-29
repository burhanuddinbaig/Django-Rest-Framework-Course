from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsStaffEditorPermission(permission.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        if user.is_staff:
            if user.has_perm("products.add_product"):
                return True
            if user.has_perm("products.delete_product"):
                return True
            if user.has_perm("products.change_product"):
                return True
            if user.has_perm("products.view_product"):
                return True
            return False
        print(user.get_all_permissions())
        return False
    
    