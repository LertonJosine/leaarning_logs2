from django.http import HttpResponse
from django.urls import path
from .views import login_page

urlpatterns = [
    path('users/', login_page, name='login_page')
]
