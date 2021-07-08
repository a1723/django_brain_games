import collections as coll


def get_prime_correct_answer(result_values, num):
    correct_values = [1, num]
    if (coll.Counter(result_values) == coll.Counter(correct_values)):
        return "yes"
    return "no"


def get_number_divisors(num):
    i = 1
    result_values = []
    while (num >= i):
        if (num % i == 0):
            result_values.append(i)
        i += 1
    return result_values
