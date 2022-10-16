
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import my_logout_view
from learning_logs.views import home
from .views import registrar
urlpatterns = [
    # path('', include('django.contrib.auth.urls')),
    # path('', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name='login' ), # type: ignore
    path('logout/', my_logout_view, name='logout'),  # type: ignore
    path('', home , name='home'),
    path('register/', registrar, name='registrar'),   # type: ignore
]
