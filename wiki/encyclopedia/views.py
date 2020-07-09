from django.shortcuts import render, redirect
from django.http import HttpResponse , HttpResponseRedirect
import markdown2
from django import forms
from . import util
import re
from django.urls import reverse
from random import choice




def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def search(request, title):
    
    response = util.get_entry(title)

    if response is None:

        return render(request, "encyclopedia/error.html", {
            "message" : "requested page was not found", 
        })

    
    return render(request, "encyclopedia/response.html", {
       "response" : markdown2.markdown(response),
       "title" : title
   })


def query(request):

    if request.method == "POST":

        entry = request.POST['q'].lower()

        response = util.get_entry(entry)


        if response is None:

            entries = util.list_entries()

            possible_matches = []

            for i in entries:
            
                if entry in i.lower():

                    possible_matches.append(i)

            if len(possible_matches) == 0:

                return render(request, "encyclopedia/matches.html", {
                    "no_matches" : "no results"

                })

            return render(request,  "encyclopedia/matches.html", {
                "matches" : possible_matches,
            })
            
        
        return render(request, "encyclopedia/response.html", {
       "response" : markdown2.markdown(response),
       "title" : entry
        })



def newpage(request):

    if request.method == "POST":

        new_page = request.POST

        title = new_page["newpage_title"]

        content= new_page['newpage_content']

        entries = util.list_entries()

        for entry in entries:

            if entry.lower() == title.lower():

                return render(request, "encyclopedia/error.html", {

                    "message": "title already exists"
                })

        util.save_entry(title,content)

    return render(request, "encyclopedia/newpage.html")


def editpage(request, entry):

    if request.method == "POST":

        new_content = request.POST['edited_content']

        util.save_entry(entry, new_content)

        return HttpResponseRedirect(reverse("encyclopedia:search", kwargs={"title" : entry}))

    markdown = util.get_entry(entry)

    return render(request, "encyclopedia/editpage.html" ,{

        "title": entry,
        "content" : markdown,

    })


def random(request):

    entries = util.list_entries()

    random = choice(entries)

    content = util.get_entry(random)

    return render(request, "encyclopedia/response.html" , {

        "title": random,
        "response": markdown2.markdown(content),
    })




