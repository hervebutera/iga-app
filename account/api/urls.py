from django.urls import path
from account.api.views import (
    registration_view,
)

from rest_framework.authtoken.views import obtain_auth_token


app_name = "account"

urlpatterns = [
    path('register', registration_view, name="register"), 
    # /user/account/register   API for creating a new user account

    path('login', obtain_auth_token, name="login"), 
    # /user/account/login API for login
]

