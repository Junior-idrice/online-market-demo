from django.urls import path
from . import views
from cs50wL8 import settings
from django.conf.urls.static import static

urlpatterns = [
     path('', views.home)
]
