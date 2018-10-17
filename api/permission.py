from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
	message="You need to hustle and become an owner yourself!"
	def has_object_permission(self,request,view,obj):
		if request.user.is_staff or obj.owner==request.user:
			return True
		return False	