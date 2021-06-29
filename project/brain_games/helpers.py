import random


WRONG_ANSWER = ' is wrong answer ;(. Correct answer was '
MAX_ROUNDS = 3


def generate_number():
    return random.randint(2, 30)


def generate_progression():
    step = random.randint(1, 5)
    progression = []
    for i in range(1, 100, step):
        progression.append(i)
    return progression


# Аргументы необязательны для универсальности и использованияя
# функции во всех играх кроме brain_gcd (из-за ненадобности пробела)
def get_user_answer(num1, num2='', operation=''):
    return prompt.string(f'Question: {num1} {operation} {num2}\nYour answer: ')


def check_answer(answer, correct_answer, rounds, player_name):
    while (answer != correct_answer):
        print(f'{answer}{WRONG_ANSWER}{correct_answer}\nLet\'s try again, {player_name}!')
        return rounds
    else:
        print('Correct!')
        rounds += 1
        return rounds


def get_congratulations(player_name, rounds):
    print(f'Congratulations, {player_name}!')
    return rounds
    