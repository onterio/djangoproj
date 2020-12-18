from django.urls import path
from . import views

urlpatterns = [
    path("", views.AuthorViews.as_view())
]