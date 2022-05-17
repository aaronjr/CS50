from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("<int:id>", views.listing, name="listing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("categorylist", views.categorylist, name="categorylist"),
    path("categorylist/<str:id>", views.categorylistitem, name="categorylistitem"),
    path("makelive", views.makelive, name="makelive"),
    path("close", views.close, name="close"),
    path("bid/<str:id>", views.bid, name="bid"),
    path("mylistings", views.mylistings, name="mylistings"),
    path("pagenotfound", views.pagenotfound, name="pagenotfound"),
    path("comment/<int:id>", views.comment, name="comment")
    
]