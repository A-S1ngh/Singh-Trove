from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *


def index(request):
    return render(request, "auctions/index.html")


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


@login_required
def createlisting(request):
    if request.method == "POST":
        listing = Listing()
        listing.name = request.POST.get('name')
        listing.category = request.POST.get('category')
        listing.startingbid = request.POST.get('startingbid')
        listing.description = request.POST.get('description')
        if request.POST.get('image'):
            listing.image = request.POST.get('image')
        else:
            listing.image = "https://www.brdtex.com/wp-content/uploads/2019/09/no-image-480x480.png"
        listing.save()
        allitems = Listing.objects.all()
        return render(request, "auctions/activelistings.html", {
            "allitems": allitems
        })
    else:
        return render(request, "auctions/createlisting.html")


@login_required
def activelistings(request):
    allitems = Listing.objects.all()
    noitems = False
    if len(allitems) == 0:
        noitems = True
    return render(request, "auctions/activelistings.html", {
        "allitems": allitems,
        "noitems": noitems
    })


def viewlisting(request, product_id):
    listing = Listing.objects.get(id = product_id)
    return render(request, "auctions/viewlisting.html", {
        "listing": listing
    })

def addtowl(request, product_id):
    if request.user.username:
        w = Watchlist()
        w.user = request.user.username
        w.listingid = product_id
        w.save()
        return redirect('viewlisting', id=product_id)
    else:
        return redirect('index')


def watchlist(request):
    pass
