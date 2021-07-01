from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from .helpers import *

def index(request):
    return render(request, 'index.html')


def game_selection(request):
    user = User()
    user.name = request.POST.get("name")
    user.save()
    return HttpResponse(render(request, 'game_selection.html', {"user": user.name}))


def first_game(request):
    num1 = generate_number()
    return render(request, 'first_game.html', context={"num1": num1})


def checking_game_answer(request):
    rounds = 0
    while rounds < MAX_ROUNDS:
        num1 = request.POST.get("num1")
        answer = AnswerForm()
        answer = request.POST.get("answer")
        correct_answer = get_correct_answer(int(num1))
        if answer == correct_answer:
            rounds += 1
            return HttpResponseRedirect("/first_game")
        else:
            return HttpResponse(render(request, "game_abort.html", context={"correct_answer":correct_answer, "answer": answer}))
    return HttpResponse(render(request, "game_congrats.html"))


def game_result(request, answer):
    answer = checking_game_answer()
    data = {"answer": answer}
    return HttpResponse(request, 'game_result.html', context=data)

