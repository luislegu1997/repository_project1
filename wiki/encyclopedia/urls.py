from django.urls import path

from . import views



app_name = "encyclopedia"
urlpatterns = [
    
    path("", views.index, name="index"),
    path("query", views.query, name="query"),
    path("search-<str:title>", views.search, name="search"),
    path("newpage", views.newpage, name="newpage"),
    path("editpage-<str:entry>", views.editpage, name="editpage"),
    path("random", views.random, name="random"),
]
