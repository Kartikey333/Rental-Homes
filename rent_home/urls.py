from django.urls import path
from . import views


urlpatterns = [
    path("house/<int:id> ", views.house_index, name="house_index"),
    path("", views.room_index, name="room_index"),
    path("details/", views.room_details, name="room_details"),
]
