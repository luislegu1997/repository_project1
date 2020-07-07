from django.urls import path

from . import views



app_name = "encyclopedia"
urlpatterns = [
    
    path("", views.index, name="index"),
    path("query", views.query, name="query"),
    path("search-<str:title>", views.search, name="link"),
    path("newpage", views.newpage, name="newpage"),
]
