from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .helpers import MAX_ROUNDS
from .forms import AnswerForm
from .brain_even_helpers import get_even_correct_answer
from .brain_calc_helpers import get_calc_correct_answer, get_operation_type
from .brain_gcd_helpers import get_gcd_correct_answer
from .brain_prime_helpers import get_prime_correct_answer, get_number_divisors
from .brain_progression_helpers import (
    get_element_index,
    get_element_val,
    get_changed_progression
)
from .helpers import (
    get_user_name,
    generate_number,
    generate_progression,
    get_name
)


def index(request):
    name = request.session['name'] = ''
    return render(request, 'index.html', context={"name": name})


def game_selection(request):
    if request.session['name'] != '':
        name = request.session.get('name')
        return HttpResponse(render(
            request,
            'game_selection.html',
            context={"name": name}
            ))
    name = request.session['name'] = get_user_name(request)
    return HttpResponse(render(
        request,
        'game_selection.html',
        context={"name": name}
        ))


def even(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    num1 = generate_number()
    return render(
        request,
        'brain_even.html',
        context={"num1": num1, "rounds": rounds, "name": name}
        )


def calc(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    num1 = generate_number()
    num2 = generate_number()
    type = get_operation_type()
    return render(
        request,
        'brain_calc.html',
        context={
            "num1": num1,
            "num2": num2,
            "type": type,
            "rounds": rounds,
            "name": name
        })


def gcd(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    num1 = generate_number()
    num2 = generate_number()
    return render(
        request,
        'brain_gcd.html',
        context={"num1": num1, "num2": num2, "rounds": rounds, "name": name})


def prime(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    num = generate_number()
    return render(
        request,
        'brain_prime.html',
        context={
            "num": num,
            "rounds": rounds,
            "name": name
            })


def progression(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    progression = generate_progression()
    element_index = get_element_index(progression)
    element_val = get_element_val(progression, element_index)
    changed_progression = get_changed_progression(progression, element_val)
    return render(
        request,
        'brain_progression.html',
        context={
            "progression": progression,
            "changed_progression": changed_progression,
            "element_val": element_val,
            "rounds": rounds,
            "name": name
            })


def even_check(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    while rounds < MAX_ROUNDS:
        num1 = request.POST.get("num1")
        answer = AnswerForm()
        answer = request.POST.get("answer")
        correct_answer = get_even_correct_answer(int(num1))
        if answer == correct_answer:
            request.session['rounds'] = rounds + 1
            return HttpResponseRedirect("/even")
        else:
            request.session['rounds'] = 0
            name = get_name(request)
            return HttpResponse(render(
                request,
                "game_abort.html",
                context={
                    "correct_answer": correct_answer,
                    "answer": answer,
                    "rounds": rounds,
                    "name": name
                }))
    del request.session['rounds']
    rounds = request.session.get('rounds', 0)
    return HttpResponse(render(
        request,
        "game_congrats.html",
        context={"name": name}))


def calc_check(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    while rounds < MAX_ROUNDS:
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        type = request.POST.get("type")
        answer = AnswerForm()
        answer = request.POST.get("answer")
        correct_answer = get_calc_correct_answer(type, int(num1), int(num2))
        if answer == correct_answer:
            request.session['rounds'] = rounds + 1
            return HttpResponseRedirect("/calc")
        else:
            request.session['rounds'] = 0
            name = get_name(request)
            return HttpResponse(render(
                request,
                "game_abort.html",
                context={
                    "correct_answer": correct_answer,
                    "answer": answer,
                    "rounds": rounds,
                    "name": name
                    }))
    del request.session['rounds']
    rounds = request.session.get('rounds', 0)
    return HttpResponse(render(
        request,
        "game_congrats.html",
        context={"name": name}))


def gcd_check(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    while rounds < MAX_ROUNDS:
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        answer = AnswerForm()
        answer = request.POST.get("answer")
        correct_answer = get_gcd_correct_answer(int(num1), int(num2))
        if answer == correct_answer:
            request.session['rounds'] = rounds + 1
            return HttpResponseRedirect("/gcd")
        else:
            request.session['rounds'] = 0
            name = get_name(request)
            return HttpResponse(render(
                request,
                "game_abort.html",
                context={
                    "correct_answer": correct_answer,
                    "answer": answer,
                    "rounds": rounds,
                    "name": name
                    }))
    del request.session['rounds']
    rounds = request.session.get('rounds', 0)
    return HttpResponse(render(
        request,
        "game_congrats.html",
        context={"name": name}))


def prime_check(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    while rounds < MAX_ROUNDS:
        num = generate_number()
        result_values = get_number_divisors(num)
        answer = AnswerForm()
        answer = request.POST.get("answer")
        correct_answer = get_prime_correct_answer(result_values, int(num))
        if answer == correct_answer:
            request.session['rounds'] = rounds + 1
            return HttpResponseRedirect("/prime")
        else:
            request.session['rounds'] = 0
            name = get_name(request)
            return HttpResponse(render(
                request,
                "game_abort.html",
                context={
                    "correct_answer": correct_answer,
                    "answer": answer,
                    "rounds": rounds,
                    "name": name
                    }))
    del request.session['rounds']
    return HttpResponse(render(
        request,
        "game_congrats.html",
        context={"name": name}))


def progression_check(request):
    rounds = request.session.get('rounds', 0)
    name = get_name(request)
    while rounds < MAX_ROUNDS:
        answer = AnswerForm()
        answer = request.POST.get("answer")
        correct_answer = request.POST.get("element_val")
        if answer == correct_answer:
            request.session['rounds'] = rounds + 1
            return HttpResponseRedirect("/progression")
        else:
            request.session['rounds'] = 0
            name = get_name(request)
            return HttpResponse(render(
                request,
                "game_abort.html",
                context={
                      "correct_answer": correct_answer,
                      "answer": answer,
                      "rounds": rounds,
                      "name": name
                      }))
    del request.session['rounds']
    rounds = request.session.get('rounds', 0)
    return HttpResponse(render(
        request,
        "game_congrats.html",
        context={"name": name}))
