from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models
# from pyparsing import FollowedBy

#user with a profile picture
class User(AbstractUser):
    image = models.URLField(null=True)
    pass

# post with content, user and date
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField() 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    count = models.IntegerField(default=0)

# user liking and post itself
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = "likedpost")

# ee is the target - er is the stalker
class Following(models.Model):
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "followee")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "stalker")