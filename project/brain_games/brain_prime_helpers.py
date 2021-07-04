import collections as coll

from .helpers import *
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .helpers import MAX_ROUNDS

def get_brain_prime_correct_answer(result_values, num):
    correct_values = [1, num]
    if (coll.Counter(result_values) == coll.Counter(correct_values)):
        return "yes"
    return "no"


def get_number_divisors(num):
    i = 1
    result_values = []
    while (num >= i):
        if (num % i == 0):
            result_values.append(i)
        i += 1
    return result_values


def checking_brain_prime_game_answer(request):
    rounds = request.session.get('rounds', 0)
    #name = get_user_name(request)
    while rounds < MAX_ROUNDS:
        num = generate_number()
        result_values = get_number_divisors(num)
        answer = AnswerForm()
        answer = request.POST.get("answer")
        correct_answer = get_brain_prime_correct_answer(result_values, int(num))
        if answer == correct_answer:
            request.session['rounds'] = rounds + 1
            return HttpResponseRedirect("/brain-prime")
        else:
            request.session['rounds'] = 0
            return HttpResponse(render(request, "game_abort.html", context={"correct_answer":correct_answer, "answer": answer, "rounds": rounds}))
    del request.session['rounds']
    return HttpResponse(render(request, "game_congrats.html"))


