from django.shortcuts import render
from django.http import HttpResponse
import markdown2

from . import util

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


    
    return render(request, "encyclopedia/response.html",
   {
       "response" : markdown2.markdown(response),
       "title" : title
   })

   # return HttpResponse("Hello, world!")



