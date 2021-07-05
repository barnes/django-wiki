from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("entry/<str:title>", views.entry, name="entry"),
    path("random", views.randEntry, name="random"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("search", views.search, name="search")
]
