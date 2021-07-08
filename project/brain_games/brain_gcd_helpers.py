
def get_gcd_correct_answer(num1, num2):   # проверяем число на чётность
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return (str(num1 + num2))
