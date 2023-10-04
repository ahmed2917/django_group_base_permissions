from django.urls import path
from account_management.views import *

urlpatterns = [
    path('signin/', SignInViews.as_view({'post': 'create'})),
]
