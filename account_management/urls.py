from django.urls import path
from account_management.views import *

urlpatterns = [
    path('signup/', SignUpViews.as_view({'post': 'create'})),
    path('signin/', SignInViews.as_view({'post': 'create'})),

    path('user/', UserViews.as_view({'get': 'list',
                                     'patch': 'update',
                                     "post": "create",
                                     "delete": "destroy"})),

    path('group/create/', GroupViews.as_view({'post': 'create'})),

]
