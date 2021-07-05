from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from brain_games.models import User, Answer
from .forms import *
from .helpers import *
from .brain_even_helpers import *
from .brain_calc_helpers import *
from .brain_gcd_helpers import *
from .brain_prime_helpers import *
from .brain_progression_helpers import *

def index(request):
    name = request.session['name'] = ''
    return render(request, 'index.html', context={"name": name})


def game_selection(request):
    if request.session['name'] != '':
        name = request.session.get('name')
        return HttpResponse(render(request, 'game_selection.html', context={"name": name}))
    name = request.session['name'] = get_user_name(request)
    return HttpResponse(render(request, 'game_selection.html', context={"name": name}))


def brain_even(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    num1 = generate_number()
    return render(request, 'brain_even.html', context={"num1": num1, "rounds": rounds, "name": name})


def brain_calc(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    num1 = generate_number()
    num2 = generate_number()
    operation_type = get_operation_type()
    return render(request, 'brain_calc.html', context={"num1": num1, "num2": num2, "operation_type": operation_type, "rounds": rounds, "name": name})


def brain_gcd(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    num1 = generate_number()
    num2 = generate_number()
    return render(request, 'brain_gcd.html', context={"num1": num1, "num2": num2, "rounds": rounds, "name": name})


def brain_prime(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    num = generate_number()
    return render(request, 'brain_prime.html', context={"num": num, "rounds": rounds, "name": name})


def brain_progression(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    progression = generate_progression()
    element_index = get_element_index(progression)
    element_val = get_element_val(progression, element_index)        
    changed_progression = get_changed_progression(progression, element_val)
    return render(request, 'brain_progression.html', context={"progression": progression, "changed_progression": changed_progression, "element_val": element_val, "rounds": rounds, "name": name})