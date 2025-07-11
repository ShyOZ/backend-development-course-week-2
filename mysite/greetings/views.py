from django.shortcuts import render, redirect
from .forms import GreetGuest


def homepage(response):
    if response.method == "POST":
        form = GreetGuest(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            return redirect(f"{name}/")

    else:
        form = GreetGuest()
        return render(response, "home.html", {"form": form})


def display_message(response, name):
    return render(response, "message.html", {"name": name})
