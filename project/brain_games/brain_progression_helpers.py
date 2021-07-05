from random import randint

from .helpers import *
from .forms import *
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .helpers import MAX_ROUNDS

def get_element_index(progression):
    element_index = randint(0, len(progression))
    return element_index


def get_element_val(progression, element_index):
    element_val = str(progression[element_index])
    return element_val


def get_changed_progression(progression, element_val):
    progression = " ".join(map(str, progression))
    changed_progression = progression.replace(str(element_val), '..', 1)
    return changed_progression


def checking_brain_progression_game_answer(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    while rounds < MAX_ROUNDS:
        progression = request.POST.get("progression")
        answer = AnswerForm()
        answer = request.POST.get("answer")
        correct_answer = request.POST.get("element_val")
        if answer == correct_answer:
            request.session['rounds'] = rounds + 1
            return HttpResponseRedirect("/brain-progression")
        else:
            request.session['rounds'] = 0
            name = get_name(request)
            return HttpResponse(render(request, "game_abort.html", context={"correct_answer":correct_answer, "answer": answer, "rounds": rounds, "name": name}))
    del request.session['rounds']
    rounds = request.session.get('rounds', 0)
    return HttpResponse(render(request, "game_congrats.html", context={"name": name}))
