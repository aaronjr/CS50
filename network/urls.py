
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('newpost', views.newpost, name="newpost"),
    path('user/<str:username>', views.userprofile, name="userprofile"),
    path('likepost/<int:id>', views.likepost, name="likepost"),
    path('updatefollow/<str:username>', views.updatefollow, name="updatefollow"),
    path('following', views.following, name="following"),
    path('editpost/<int:id>', views.editpost, name='editpost')
]
