from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from brain_games.models import User, Answer
from .forms import *
from .helpers import *

def index(request):
    return render(request, 'index.html')


def game_selection(request):
    name = get_user_name(request)
    return HttpResponse(render(request, 'game_selection.html', {"name": name}))


def first_game(request):
    num1 = generate_number()
    rounds = request.session.get('rounds', 0)
    return render(request, 'first_game.html', context={"num1": num1, "rounds": rounds})


def checking_game_answer(request):
    rounds = request.session.get('rounds', 0)
    name = get_user_name(request)
    while rounds < MAX_ROUNDS:
        num1 = request.POST.get("num1")
        answer = AnswerForm()
        answer = request.POST.get("answer")
        correct_answer = get_correct_answer(int(num1))
        if answer == correct_answer:
            request.session['rounds'] = rounds + 1
            return HttpResponseRedirect("/first-game")
        else:
            return HttpResponse(render(request, "game_abort.html", context={"correct_answer":correct_answer, "answer": answer, "rounds": rounds}))
    del request.session['rounds']
    rounds = request.session.get('rounds', 0)
    return HttpResponse(render(request, "game_congrats.html", {"name": name}))


def game_result(request, answer):
    answer = checking_game_answer()
    data = {"answer": answer}
    return HttpResponse(request, 'game_result.html', context=data)

