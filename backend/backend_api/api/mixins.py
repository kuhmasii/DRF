from .permissions import IsStaffEditorPermission
from rest_framework.permissions import IsAdminUser
from django.conf import settings


class StaffEditorPermissionMixin():
	if not settings.DEBUG:
	    permission_classes = [IsAdminUser, IsStaffEditorPermission]
