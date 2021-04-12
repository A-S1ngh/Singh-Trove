from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting", views.createlisting, name="createlisting"),
    path("activelistings", views.activelistings, name="activelistings"),
    path("viewlisting/<int:product_id>", views.viewlisting, name="viewlisting"),
    path("addtowl/<int:product_id>", views.addtowl, name="addtowl"),
    path("watchlist", views.watchlist, name="watchlist"),

]
