from django.http import HttpResponse
from django.urls import path, include
from .views import accounts

urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    path('', accounts, name="accounts"),
]
