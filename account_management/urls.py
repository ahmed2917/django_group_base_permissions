from django.urls import path
from account_management.views import *

urlpatterns = [
    path('signup/', UserViews.as_view({'post': 'create'})),
]
