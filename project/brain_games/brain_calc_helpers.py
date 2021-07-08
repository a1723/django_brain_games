import operator
import random


operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
}


def get_operation_type():
    return random.choice(list(operations.keys()))


def get_calc_correct_answer(type, num1, num2):
    return str(operations[type](num1, num2))
