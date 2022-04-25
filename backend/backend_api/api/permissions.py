from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):

	perms_map = {
		'GET':['%(app_label)s.view_%(model_name)s'],
		'OPTIONS': [],
		'HEAD':[],
		'POST':['%(app_label)s.add_%(model_name)s'],
		'PUT':['%(app_label)s.change_%(model_name)s'],
		'PATCH':['%(app_label)s.change_%(model_name)s'],
		'DELETE':['%(app_label)s.delete_%(model_name)s']
	}

	# def has_permission(self, request, view):
	# 	if not request.user.is_staff:
	# 		return False
	# 	return super().has_permission(request, view)
	# not fully giving the permissions function <|>

	# checking if the view has any other related permissions
	# def has_permission(self, request, view):
	# 	user = request.user
	# 	if user.is_staff:
	# 		if user.has_perm('school.add_school'):
	# 			return True 
	# 		if user.has_perm('school.delete_school'):
	# 			return True
	# 		if user.has_perm('school.change_product'):
	# 			return True
	# 		if user.has_perm('school.view_school'):
	# 			return True
	# 		return False
	# 	return False



	# def has_object_permission(self, request, view, obj):
	# 	# checking if the view has permissions going down to obj level.
	# 	return obj.owner == request.user


