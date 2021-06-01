from django.contrib import admin
from users.models import Profile, TeacherRequests
# Register your models here.

admin.site.register(Profile)
admin.site.register(TeacherRequests)
