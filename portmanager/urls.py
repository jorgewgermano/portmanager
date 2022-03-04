from urllib.parse import urlparse
from django.urls import path
from portmanager.views import home

urlpatterns = [
    path('',home),
]
