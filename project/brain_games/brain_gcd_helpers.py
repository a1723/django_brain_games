from .helpers import *
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .helpers import MAX_ROUNDS


def get_brain_gcd_correct_answer(num1, num2):   # проверяем число на чётность
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return (str(num1 + num2))


def checking_brain_gcd_game_answer(request):
    rounds = request.session.get('rounds', 0)
    #name = get_user_name(request)
    while rounds < MAX_ROUNDS:
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        answer = AnswerForm()
        answer = request.POST.get("answer")
        correct_answer = get_brain_gcd_correct_answer(int(num1), int(num2))
        if answer == correct_answer:
            request.session['rounds'] = rounds + 1
            return HttpResponseRedirect("/brain-gcd")
        else:
            request.session['rounds'] = 0
            return HttpResponse(render(request, "game_abort.html", context={"correct_answer":correct_answer, "answer": answer, "rounds": rounds}))
    del request.session['rounds']
    rounds = request.session.get('rounds', 0)
    return HttpResponse(render(request, "game_congrats.html"))
