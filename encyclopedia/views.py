from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from . import util

class NewEntryForm(forms.Form):
    title = forms.CharField(label="Entry Title")
    entry = forms.CharField(label="Entry Content", widget=forms.Textarea)

entryList = util.list_entries()
print(entryList)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def add(request):
    if request.method == "POST":
        form = NewEntryForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["title"] not in entryList:
                util.save_entry(form.cleaned_data["title"],form.cleaned_data["entry"])
                return HttpResponseRedirect(reverse("encyclopedia:index"))
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
    


    

