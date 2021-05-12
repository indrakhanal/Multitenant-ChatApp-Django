from django.urls import path, include
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('login/', login_public, name='login'),
    path('logout/', logout_public, name='logout'),
]

