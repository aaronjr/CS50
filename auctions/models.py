from tkinter import CASCADE
from unicodedata import category
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import datetime    

categories_choices = [
        ("Shoes", "Shoes"),
        ("Clothes", "Clothes"),
        ("Homeware", "Homeware"),
        ("Car", "Car"),
        ("Baby", "Baby"),
        ("Toys", "Toys"),
        ("Electronics", "Electronics")
]

class User(AbstractUser):
   pass

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    price = models.FloatField(blank=True)

class Listing(models.Model):
    listuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listuser")
    item = models.CharField(max_length=64)
    price = models.FloatField()
    date = models.DateTimeField()
    description = models.CharField(max_length=140)
    category = models.CharField(max_length=12, choices=categories_choices, null=False)
    image = models.URLField()
    winner = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)

    def __str__(self):
        return f"Item listed:{self.item} Description:{self.description}"

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_watch = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="watchlist")

class Comment(models.Model):
    commentuser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usercomment")
    listitem = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listcomment")
    comment = models.CharField(max_length=140)
    date = models.DateTimeField()

class Auction(models.Model):
    listauction = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE, null=True, blank=True, related_name="bid")
    status = models.BooleanField(default=True)
    