from hashlib import new
from django.core import exceptions
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from . import util
import random

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Entry Title")
    entry = forms.CharField(label="Entry Content", widget=forms.Textarea)


entryList = util.list_entries()



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "entry": util.get_entry(title)
    })

def randEntry(request):
    randTitle = random.choice(entryList)
    return render(request, "encyclopedia/entry.html", {
        "title": randTitle,
        "entry": util.get_entry(randTitle)

    })

def edit(request, title):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            util.save_entry(form.cleaned_data["title"],form.cleaned_data["entry"])
            return HttpResponseRedirect(reverse("encyclopedia:entry", args=[title]))
        else:
            return render(request, "encyclopedia/edit.html", {
                "form": form
            })
    return render(request, "encyclopedia/edit.html", {
        "form": NewEntryForm({
            "title": title,
            "entry": util.get_entry(title)
        }),
        "title": title
    })


def add(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["title"] not in entryList:
                util.save_entry(form.cleaned_data["title"],form.cleaned_data["entry"])
                return HttpResponseRedirect(reverse("encyclopedia:entry", args=[form.cleaned_data["title"]]))
            else:
                return render(request, "encyclopedia/add.html", {
                "form": form,
                "error": "Entry already exists."
            })
        else:
            return render(request, "encyclopedia/add.html", {
                "form": form
            })

    return render(request, "encyclopedia/add.html", {
        "form": NewEntryForm()
    })

def search(request):
    query = request.POST["q"]
    if request.method == "POST":
        if query in entryList:
            return render(request, "encyclopedia/entry.html", {
                "title": query,
                "entry": util.get_entry(query)
            })
        else:
            res = [i for i in entryList if query in i]
            print(query)
            print(res)
            return render(request, "encyclopedia/search.html", {
                "entries": res
            })


    


    

