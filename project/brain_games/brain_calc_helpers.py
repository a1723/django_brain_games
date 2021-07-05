import operator
import random
from .helpers import *
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from .helpers import *

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}

def get_operation_type():
    return random.choice(list(operations.keys()))


def get_brain_calc_correct_answer(operation_type, num1, num2):
    return str(operations[operation_type](num1, num2))

def checking_brain_calc_game_answer(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    while rounds < MAX_ROUNDS:
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        operation_type = request.POST.get("operation_type")
        answer = AnswerForm()
        answer = request.POST.get("answer")
        correct_answer = get_brain_calc_correct_answer(operation_type, int(num1), int(num2))
        if answer == correct_answer:
            request.session['rounds'] = rounds + 1
            return HttpResponseRedirect("/brain-calc")
        else:
            request.session['rounds'] = 0
            name = get_name(request)
            return HttpResponse(render(request, "game_abort.html", context={"correct_answer":correct_answer, "answer": answer, "rounds": rounds, "name": name}))
    del request.session['rounds']
    rounds = request.session.get('rounds', 0)
    return HttpResponse(render(request, "game_congrats.html", context={"name": name}))