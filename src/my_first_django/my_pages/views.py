from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def home_view(*args, **kwargs):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def contact_view(*args, **kwargs):
    return HttpResponse("Contact Page")

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123
    }
    return render(request, "about.html", my_context)