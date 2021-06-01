from django.urls import path

from users.views import Profile, teacher_request

app_name = 'users'

urlpatterns = [
    path('profile/', Profile, name='profile'),
    path('teacher_request/', teacher_request, name='teacher_request')

]
