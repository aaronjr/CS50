from ast import Str
from multiprocessing.dummy.connection import families
from nis import cat
from this import d
from unicodedata import category
from xmlrpc.client import boolean
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms
from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime

from .models import User, Listing, Watchlist, categories_choices, Auction, Bid, Comment

def index(request):
    # load all active listings from the auction.
    auction = Auction.objects.filter(status = True)
    return render(request, "auctions/index.html",{
        "auctions":auction,
    })

@login_required
def mylistings(request):
    # find all listings posted by this user whether live or not
    listings = Listing.objects.filter(listuser = request.user)
    return render(request, "auctions/mylistings.html",{
        "listings":listings,
    })

@login_required
def create(request):
    # when form is submitted.. 
    if request.method == "POST":
        
        emplist = []
        for cat in categories_choices:
            emplist.append(cat[1])

        if request.POST["category"] not in emplist:
            messages.error(request, "Must select a catrogry from the list provided.")
            return redirect("create")

        # save all data from the form and save accordingly
        a = Listing.objects.create(
            listuser = request.user,
            item = request.POST["itemname"],
            price = round(float(request.POST["price"]),2),
            description = request.POST["description"],
            image = request.POST["image"],
            date = datetime.now(),
            category = request.POST["category"]
            )
        
        # when item is created, by deafult it will be made live
        Auction.objects.create(listauction_id = a.id)

        # redirect to index, index will load all live listings. 
        return redirect("index")
    else:
        # on a get request load the form to make a new listing
        return render(request, "auctions/create.html", {
            "form":CreateListing(),
        })

def listing(request, id):
    if request.method == "GET":
        # load listing and if possible auction listing
        listings = Listing.objects.get(pk = id)
        try:
            auctions = Auction.objects.get(listauction__id = id, status = True)
        except ObjectDoesNotExist:
            auctions = None 

        # if user logged in, check for the watchlist and update WLIST accordingly
        if request.user.is_authenticated:
            list = Watchlist.objects.filter(item_watch = id, user = request.user)
            if not list:
                wlist = "N"
            else:
                wlist = "Y"
        else:
            wlist = False

        comments = Comment.objects.filter(listitem_id = id).order_by('-date')

        # load the render
        return render(request, "auctions/listing.html", {
            "id": id,
            "wlist": wlist,
            "listing": listings,
            "auction": auctions,
            "bidform": BidForm(),
            "comments":comments,
            "commentform":CommentForm
        })
    else:
        # not possible but is somehow managed, redirect to index.
        redirect("index")

@login_required
def watchlist(request):
    # when loading the page, search for live auctions the user has added to watchlist
    if request.method == "GET":
        auction = Auction.objects.filter(listauction__watchlist__user = request.user, status = True)
        return render(request, "auctions/watchlist.html",{
            "auctions":auction,
        })

    # to add a new item to the watchlist
    if request.method == "POST":
        id = request.POST["id"]
        username = request.user
        # find the requested listing
        listings = Listing.objects.get(pk = id)
        
        # either add to watchlist, or if already present remove
        user = Watchlist.objects.filter(item_watch = id)
        if not user:
            Watchlist.objects.create(user = username, item_watch = listings)
        else:
            Watchlist.objects.filter(item_watch = id).delete()

        # load updated list of watchlist items
        auction = Auction.objects.filter(listauction__watchlist__user = username, status = True)
        return redirect("listing", id)

def categorylist(request):
    # load a list of possible categories
    if request.method == "GET":
        list = []
        for choice in categories_choices:
            list.append(choice[1])
    return render(request, "auctions/category.html",{
        "choices":list
    })

def categorylistitem(request, id):
    # get all items from a paticular category and display on page
     if request.method == "GET":
         # check if what has been searched is a category, redirect to page not found.
        list = []
        for choice in categories_choices:
            list.append(choice[1])
        if id not in list:
            return redirect("pagenotfound")
        # if search is a category load as appropriate
        else:
            auctions = Auction.objects.filter(listauction__category = id, status = True)
            return render(request, "auctions/categoryitem.html", {
            "id": id,
            "auctions": auctions
        })

@login_required
def makelive(request):
    # will link a listing to auction, it will default as status within the 
    # model to be True, therefore active
    if request.method == "POST":
        Auction.objects.create(listauction_id = request.POST["action"])
        return redirect("index")
    # not possible to get from, so will refirect to index
    else:
        return redirect("index")

def close(request):
    if request.method == "POST":
        # try to check if any exisitng bids on item, and update a winner for when it gets closed
        try:
            a = Bid.objects.get(bid__listauction_id = request.POST["action"], bid__status = True)
            Listing.objects.filter(id = request.POST["action"]).update(winner = a.user)
        except ObjectDoesNotExist:
            pass
        
        # Update listing to closed and delete exisiting bids - already saved winner if relevant
        Auction.objects.filter(listauction_id = request.POST["action"]).update(status = False)
        Bid.objects.filter(bid__listauction_id = request.POST["action"]).delete()
        
        # Delete comments from when listing was live
        Comment.objects.filter(listitem_id = request.POST["action"]).delete()

        # remove exisiting entrys where this item is being watched by other users
        Watchlist.objects.filter(item_watch_id = request.POST["action"]).delete()
        return redirect("index")
    else:
        return redirect("index")

@login_required
def bid(request,id):
    if request.method == "POST":
        # load bid amount from form
        checkbid = Auction.objects.get(listauction_id = id, status = True)
        # get start price
        checkprice = Listing.objects.get(id = id)
        # check if exisisting bids
        try:
            a = checkbid.bid.price
        except AttributeError:
            a = None

        # if no current bids, and first bid is same or higher than starting price, bid accepted
        if a == None and float(request.POST["bid"]) >= checkprice.price:
            a = Bid.objects.create(price = request.POST["bid"], user = request.user,)
            Auction.objects.filter(listauction_id = id).update(bid = a.id)
            return redirect("listing", id)
        # else if there is a current bid, bid must be higher than this bid - 
        # or if no exisitng bid, first bid must be same or higher than starting price
        elif a != None and float(request.POST["bid"]) <= checkbid.bid.price or float(request.POST["bid"]) < checkprice.price:
                messages.error(request, "Bid must be higher than current price")
                return redirect("listing", id)
        # if no current bids save.
        else:
            a = Bid.objects.create(price = round(float(request.POST["bid"]),2), user = request.user,)
            Auction.objects.filter(listauction_id = id).update(bid = a.id)
            return redirect("listing", id)

    else:
        return redirect("listing", id)

def pagenotfound(request):
    # if page can not be found, load standard page not found screen
    return render(request, "auctions/pagenotfound.html",{
    })

@login_required
def comment(request, id):
    if request.method == "POST":
        comment = request.POST["comment"]
        user = request.user

        Comment.objects.create(
            commentuser = user, 
            comment = comment, 
            listitem_id = id,
            date = datetime.now()
            )
        return redirect("listing", id)
    else:
        return redirect("index")

# form for creating a new item
class CreateListing(forms.Form):
    itemname = forms.CharField(widget= forms.TextInput
                           (attrs={'class':'form-control'}),label="Item name:")
    price = forms.FloatField(label='Starting price',
                widget=forms.NumberInput(attrs={'class':'form-control'})) 
    description = forms.CharField(widget= forms.TextInput
                           (attrs={'class':'form-control'}),label="Description:")
    image = forms.CharField(widget= forms.TextInput
                           (attrs={'class':'form-control'}),label="Image URL:", max_length=200)
    category = forms.CharField(max_length=12,widget=forms.Select(choices=categories_choices, attrs={'class':'form-control'}))
    
# form for a new bid
class BidForm(forms.Form):
    bid = forms.FloatField(label='', required=False,
            widget=forms.NumberInput(attrs={'placeholder': ('Bid'),'class':'form-control formwidth bid'})) 

class CommentForm(forms.Form):
    comment = forms.CharField(label=False, widget = forms.Textarea(attrs={'placeholder': 'Comment', 'class':'form-control formwidth commentbox', 'rows':'3', 'cols':'5'}), max_length=140)
# pre-installed views #

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))