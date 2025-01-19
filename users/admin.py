from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User

admin.site.unregister(User)

# Register the default User model with the default UserAdmin
admin.site.register(User, UserAdmin)

