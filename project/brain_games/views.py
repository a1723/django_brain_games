from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .helpers import *

def index(request):
    nameForm = NameForm()
    if request.method == "POST":
        nameForm = NameForm(request.POST)
        if nameForm.is_valid():
            name = request.POST.get("name")
            data = {"name": name}
            return HttpResponse(render(request, "game_selection.html", context=data))
    return render(request, "index.html")


def game_selection(request):
    return HttpResponse(request, 'game_selection.html')


def get_answer(request):
    answer = request.POST.get("answer")
    answer = {"answer": answer}
    return HttpResponse(render(request, 'game_answer.html', context=answer))


def game(request):
    AnswerForm()
    num1 = generate_number()
    data = {"num1": num1}
    return HttpResponse(render(request, "first_game.html", context=data))


def game_result(request, answer):
    answer = get_answer()
    data = {"answer": answer}
    return HttpResponse(request, 'game_result.html', context=data)


"""def get_correct_answer(num1):   # проверяем число на чётность
    return "yes" if (num1 % 2 == 0) else "no"


def brain_even(player_name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    rounds = 0
    correct_rounds = 0
    while rounds < MAX_ROUNDS:
        num1 = generate_number()
        answer = get_user_answer(num1)
        correct_answer = get_correct_answer(num1)
        correct_rounds = check_answer(answer, correct_answer, rounds, player_name)
        rounds += 1
        if (correct_rounds != rounds):
            return correct_rounds
    return correct_rounds
    get_congratulations(player_name, correct_rounds)"""