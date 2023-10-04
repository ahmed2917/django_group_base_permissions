from django.urls import path
from account_management.views import *

urlpatterns = [
    path('signup/', SignUpViews.as_view({'post': 'create'})),
    path('signin/', SignInViews.as_view({'post': 'create'})),

    path('group/create/', GroupViews.as_view({'post': 'create'})),

]
