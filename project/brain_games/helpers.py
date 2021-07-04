import random

from brain_games.models import * 

MAX_ROUNDS = 2


def generate_number():
    return random.randint(2, 30)


def get_user_name(request):
    name = request.POST.get("name")
    return name


def generate_progression():
    step = random.randint(1, 5)
    progression = []
    for i in range(1, 100, step):
        progression.append(i)
    return progression
