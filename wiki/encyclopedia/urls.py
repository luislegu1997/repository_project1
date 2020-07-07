from django.urls import path

from . import views



app_name = "encyclopedia"
urlpatterns = [
    
    path("", views.index, name="index"),
    path("query", views.query, name="query"),
    path("title-<str:title>", views.title, name="title"),
]
