from logging import PlaceHolder
from django.shortcuts import render
from django import forms
from . import util
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
import random 
import markdown2

# new form - sidebar
class NewSearchForm(forms.Form):
    search = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Search'}))

# load homepage with a list of possible entries
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(), 
        "form": NewSearchForm()
    })

# load title page
def title(request, title):
    #if url bar returns an entry that isnt available error page will load
    if util.get_entry(title) == None:
        return render (request, "encyclopedia/notfound.html",{
            "title": title,
            "form": NewSearchForm()
        })
    
    # if match - load correct page
    return render(request, "encyclopedia/title.html", {
        "content":markdown2.markdown(util.get_entry(title)),
        "title": title,
        "form": NewSearchForm()
    })

# search for match on WIKI
def search(request):
    # Check if method is POST
    if request.method == "POST":
        # Get data from search box
        title = request.POST.get("search","")
        # create three lists, two to compare with .lower()
        # one list to post for the "half word" results
        entrieslist = []
        listnewlower = []
        listnew = []

        # loop through list making lower each item
        for item in util.list_entries():
            entrieslist.append(item.lower())
            # checking for a partial match with each item also using .lower()
            # one list saved as lower another as normal
            if title.lower() in item.lower():
                listnewlower.append(item.lower())
                listnew.append(item)
        # check if search as lowercase in entries
        if title.lower() in entrieslist:
            return redirect("encyclopedia:title", title)

        elif len(listnew) > 0:
            # if atleast one match, display list of matches
            return render(request, "encyclopedia/search.html", {
                    "list": listnew,
                    "form": NewSearchForm()
                })
        else:
            # no full or partial matches display error page not finding search item.
            return render (request, "encyclopedia/notfound.html",{
                "title": title,
                "form": NewSearchForm()
            })
    # if GET load index page
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(), 
            "form": NewSearchForm()
        })

# create a new entry
def newpage(request):
    if request.method == "POST":
        # Get data from form
        title = request.POST.get("title","")
        content = request.POST.get("content","")
        # Error message - incase page already exists
        error = "Page already exists."
        # convert title to lower
        titlelower = title.lower()
        # create a list, to convert list to .lower()
        entrieslist = []
        # loop through list making lower each item
        for item in util.list_entries():
            entrieslist.append(item.lower())
            # checking for a partial match with each item also using .lower()
            # one list saved as lower another as normal

        if titlelower in entrieslist:
            return render(request, "encyclopedia/newpage.html", {
            "title":title,
            "content":content,
            "form": NewSearchForm(),
            "error": error
            })
        else:
            util.save_entry(title, content)
            return redirect("encyclopedia:title", title)
    else:
        # load empty form
        return render(request, "encyclopedia/newpage.html", {
            "form": NewSearchForm()
        })

# edit entry on page
def editpage(request, title):
    if request.method == "POST":
        # get content from post
        content = request.POST.get("content","")
        #save content and title in entry
        util.save_entry(title, content)
        return redirect("encyclopedia:title", title)
    else:
        # load content in textarea ready to be saved
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title":title,
            "content": content, 
            "form": NewSearchForm()
        })

# load a random page from entry list and redirect to it with title
def randompage(request):
    if request.method == "GET":
        l = util.list_entries()
        title = random.choice(l)
        return redirect("encyclopedia:title", title)