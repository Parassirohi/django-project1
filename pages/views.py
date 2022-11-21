from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})


def contact_view(request, *args, **kwarga):
    print(args, kwarga)
    print(request.user)
    # return HttpResponse("<h1>Contact Page</h1>")

    return render(request, "contact.html", {})


def about_view(request, *args, **kwarga):
    print(args, kwarga)
    print(request.user)
    # return HttpResponse("<h1>about Page</h1>")
    my_context = {
        "title": "This is about user",
        "this_is_true": True,
        "my_number": 1234,
        "my_list": [1234, 45678, 312, "Abc"],

    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwarga):
    print(args, kwarga)
    print(request.user)
    # return HttpResponse("<h1>Social Page</h1>")
    return render(request, "social.html", {})
