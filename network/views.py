from time import time
import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.shortcuts import redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator

from .models import User, Post, Like, Following


def index(request):
    if request.method == "GET":
        # get all posts
        posts = Post.objects.all().order_by('-date')

        # try to load which posts the user has liked - wont work if not logged in.
        try:
            user = User.objects.get(username = request.user)
            likes = Like.objects.filter(user = user).values_list("post", flat=True)
        except:
            likes = []
            User.DoesNotExist 

        # Show 10 contacts per page.
        paginator = Paginator(posts, 10) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, "network/index.html",{
            "likes":likes,
            "page_obj":page_obj
        })

def newpost(request):
    if request.method == "POST":
        # get three bits of info to save post
        content =  request.POST["content"]
        user = request.user
        date = datetime.now(tz=timezone.utc)
        # add to DB - but check to make sure length matches need
        if len(content) - 1 > 140:
            messages.error(request, "Post must not exceed 140 characters.")
            return redirect ("index")
        elif len(content) == 0:
            messages.error(request, "Post must contain at least 1 characters.")
            return redirect ("index")
        else:
            # add to DB
            Post.objects.create(user = user, date = date, content = content)

        return redirect("index")

@csrf_exempt
@login_required
def editpost(request, id):
    # get post - may fail if post doesnt exist
    try:
        post = Post.objects.get(user__username=request.user, pk=id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)

    if request.method == "POST":
        data = json.loads(request.body)
        post = data.get('post')
        print(id, post)
        Post.objects.filter(pk = id).update(content = post)
        return HttpResponse(status=204)       

def userprofile(request, username):
    if request.method == "GET":
        # get users posts
        posts = Post.objects.filter(user__username = username).order_by('-date')
        # get following and followers count
        followers = Following.objects.filter(followee__username = username).count()
        following = Following.objects.filter(follower__username = username).count()
        # get username for jinja
        user = User.objects.get(username = username)
        # count of posts
        postcount = Post.objects.filter(user__username = username).count()
        # check to see if they are or arent following the user from the profile
        followerz = Following.objects.filter(
            followee__username = username, 
            follower__username = request.user
            )

        check = []
        for follower in followerz:
            check.append(follower.follower)

        if request.user not in check:
            check = False
        else:
            check = True

        # check to see if this is the users profile.
        if str(request.user) == str(username):
            thisuser = True
        else:
            thisuser = False

        # pass which posts this user has liked - may fail if not logged in
        try:
            userz = User.objects.get(username = request.user)
            likes = Like.objects.filter(user = userz).values_list("post", flat=True)
        except:
            likes = []
            User.DoesNotExist 

        # Show 10 contacts per page.
        paginator = Paginator(posts, 10) 
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, "network/userprofile.html",{
            "page_obj":page_obj,
            "followers" : followers,
            "following" : following,
            "profile": user,
            "check": check,
            "thisuser":thisuser,
            "postcount":postcount,
            "likes":likes
        })

@csrf_exempt
@login_required
def likepost(request, id):
    if request.method == "POST":

        # get the posts the user has currently liked
        data = json.loads(request.body)
        likes = Like.objects.filter(user = request.user, post = id)

        # if they dont currently like that post then add them and update count
        if not likes:
            post = Post.objects.get(id = id)
            Like.objects.create(post = post, user = request.user)
            count = Post.objects.get(id = id)
            newcount = count.count +1
            Post.objects.filter(id = id).update(count = newcount)
            return HttpResponse(status=204)       
        # if they do currently like that post then unlike and count down like count
        else:
            Like.objects.filter(post = id, user = request.user).delete()
            count = Post.objects.get(id = id)
            newcount = count.count -1
            Post.objects.filter(id = id).update(count = newcount)
        return HttpResponse(status=204)       


def following(request):
    if request.method == "GET":
       
        # check user is logged in
        if request.user.is_anonymous:
            messages.error(request, "Not logged in")
            return render(request, "network/following.html", {
            })
        # if logged in, 
        else:    
            following = Following.objects.filter(follower = request.user)
            # put into a python list
            follow = []
            for i in following:
                follow.append(i.followee)

            # get all posts from users they follow
            posts = Post.objects.filter(user__in = follow).order_by('-date')
            # try to get, may fail if user not logged in
            try:
                user = User.objects.get(username = request.user)
                likes = Like.objects.filter(user = user).values_list("post", flat=True)
            except:
                likes = []
                User.DoesNotExist 

            # Show 10 contacts per page.
            paginator = Paginator(posts, 10) 
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            
            return render(request, "network/following.html", {
                "follow":follow,
                "page_obj":page_obj,
                "likes":likes
            })

def updatefollow(request, username):

    if request.method == "POST":
        
        # check for who they follow
        followers = Following.objects.filter(
            followee__username = username, 
            follower__username = request.user
            )
        # make into a list
        check = []
        for follower in followers:
            check.append(follower.follower)
        
        
        if request.user not in check:
            # not following so create a follow                
            followee = User.objects.get(username = username)
            follower = User.objects.get(username = request.user)
            Following.objects.create(followee = followee, follower = follower)
            return redirect("userprofile", username)
        else:
            # following so unfollow
            Following.objects.filter(followee__username = username, follower__username = request.user).delete()
            
        return redirect("userprofile", username)

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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })
        
        image = request.POST["image"]

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password, image = image)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
