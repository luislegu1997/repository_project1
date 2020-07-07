from django.shortcuts import render
from django.http import HttpResponse
import markdown2
from django import forms
from . import util
import re



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):
    
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
    #breakpoint()
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











