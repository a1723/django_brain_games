import random

from django.http.response import HttpResponse
from brain_games.models import * 


WRONG_ANSWER = ' is wrong answer ;(. Correct answer was '
MAX_ROUNDS = 2


def get_correct_answer(num1):   # проверяем число на чётность
    return "yes" if (num1 % 2 == 0) else "no"


def generate_number():
    return random.randint(2, 30)


def generate_progression():
    step = random.randint(1, 5)
    progression = []
    for i in range(1, 100, step):
        progression.append(i)
    return progression

    
def get_user_name(request):
    player = User(request.POST.get("name"))
    player.save()
    name = player.name
    return name

