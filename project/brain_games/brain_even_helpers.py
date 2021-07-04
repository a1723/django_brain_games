from .helpers import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *

def get_brain_even_correct_answer(num1):   # проверяем число на чётность
    return "yes" if (num1 % 2 == 0) else "no"


def checking_brain_even_game_answer(request):
    rounds = request.session.get('rounds', 0)
    #name = get_user_name(request)
    while rounds < MAX_ROUNDS:
        num1 = request.POST.get("num1")
        answer = AnswerForm()
        answer = request.POST.get("answer")
        correct_answer = get_brain_even_correct_answer(int(num1))
        if answer == correct_answer:
            request.session['rounds'] = rounds + 1
            return HttpResponseRedirect("/brain-even")
        else:
            request.session['rounds'] = 0
            return HttpResponse(render(request, "game_abort.html", context={"correct_answer":correct_answer, "answer": answer, "rounds": rounds}))
    del request.session['rounds']
    rounds = request.session.get('rounds', 0)
    return HttpResponse(render(request, "game_congrats.html"))