from specific.views import *
from django.urls import path

app_name='specific'

urlpatterns=[

    path('sai/',sai,name='sai'),
    path('jaya/',jaya,name='jaya'),
]