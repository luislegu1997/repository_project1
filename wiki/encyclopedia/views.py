from django.shortcuts import render
from django.http import HttpResponse
import markdown2
from django import forms
from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def title(request, title):

    #if request.method == "POST":


    
    response = util.get_entry(title)

    if response is None:

        print("wwjsjsj")

        return render(request, "encyclopedia/error.html", {
            "message" : "requested page was not found", 
        })

    
    return render(request, "encyclopedia/response.html", {
       "response" : markdown2.markdown(response),
       "title" : title
   })


def query(request):

    if request.method == "POST":

        entry = request.POST['q']

        print("hola")
        print(entry)

        response = util.get_entry(entry)


        if response is None:

             return render(request, "encyclopedia/error.html", {
            "message" : "requested ", 
        })

        return render(request, "encyclopedia/response.html", {
       "response" : markdown2.markdown(response),
       "title" : entry
        })











