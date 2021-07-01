import random


WRONG_ANSWER = ' is wrong answer ;(. Correct answer was '
MAX_ROUNDS = 3


def get_correct_answer(num1):   # проверяем число на чётность
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
    get_congratulations(player_name, correct_rounds)


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
    