from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.listTasks),
    path("tasks/<int:pk>/", views.taskDetails),
]