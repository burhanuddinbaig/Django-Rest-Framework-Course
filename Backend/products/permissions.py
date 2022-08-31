from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):    #is owner Or Read only.
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsStaffEditorPermission(permissions.DjangoModelPermissions):  # IsStaffEditorPermission
    perms_map = {
        'GET': ['%(app_label)s.add_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def permission(self, request, view):
        if not request.staff.is_staff:
            return False
        return super().has_permissions(request, view)

    # def has_permission(self, request, view):
    #     user = request.user
    #     if user.is_staff:
    #         if user.has_perm("products.add_product"):
    #             return True
    #         if user.has_perm("products.delete_product"):
    #             return True
    #         if user.has_perm("products.change_product"):
    #             return True
    #         if user.has_perm("products.view_product"):
    #             return True
    #     print(user.get_all_permissions())       # to print just permissions
    #     return False