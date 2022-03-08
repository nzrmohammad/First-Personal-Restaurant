from django.urls import path
from . import views

app_name = "Restaurant"
urlpatterns = [
    path('', views.home, name='home'),
]