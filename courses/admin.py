from django.contrib import admin
from courses.models import Class, Lesson, Subject

# Register your models here.

admin.site.register(Subject)
admin.site.register(Lesson)
admin.site.register(Class)
