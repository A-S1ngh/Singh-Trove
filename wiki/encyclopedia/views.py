from django.shortcuts import render
import markdown2
from random import choice
from django.http import HttpResponse
from django.urls import reverse
from django.core.files import File


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    mark = markdown2.Markdown()
    page = util.get_entry(title)

    if page is None:
        return render(request, "encyclopedia/error.html", {

        })

    return render(request, "encyclopedia/entry.html", {
        "title": title.capitalize(),
        "content": mark.convert(util.get_entry(title)),
    })

def add(request):
    return render(request, "encyclopedia/add.html", {
        "entries": util.list_entries()
    })

def randompage(request):
    return entry(request,choice( util.list_entries()))
