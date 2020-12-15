from django.urls import path

from . import views

app_name = 'wiki'
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry"),
    path("add", views.add, name="add"),
    path("random/", views.randompage, name="random"),

]
