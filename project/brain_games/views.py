from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm

def index(request):
    nameForm = NameForm()
    if request.method == "POST":
        nameForm = NameForm(request.POST)
        if nameForm.is_valid():
            name = request.POST.get("name")
            data = {"name": name}
            return HttpResponse(render(request, "game_selection.html", context=data))
    return render(request, "index.html")


def game(request):
        data = {"name": "test!"}
        return HttpResponse(render(request, "first_game.html", context=data))
