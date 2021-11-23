#in todo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("auth", views.auth, name="auth"), #new
    path("<int:task_id>/complete", views.complete, name="complete"), #new
    path("<int:task_id>/delete", views.delete, name="delete"), #new


]