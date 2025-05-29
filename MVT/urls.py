from django.urls import path
from . import views

app_name = 'MVT'

urlpatterns = [
    path("", views.index, name="index"),
]