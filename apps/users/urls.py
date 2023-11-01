# Django modules
from django.urls import path

# Django Views
from apps.users.views import user_login

# App name
app_name = 'users'

urlpatterns = [
    path('login/', user_login, name='login'),
]