# На воход подаются два числа. Напишите метод, который
# вернет сумму, разность, произведение и частное этих чисел.

import random

def calculate(n1, n2):
    return n1 + n2, n1 - n2, n1 * n2, n1 / n2

num_f = 9
num_s = 3
res = calculate(num_f, num_s)
summ, raznost, umnozhenie, delenie = calculate(num_f, num_s)
print(res)
print(summ, raznost, umnozhenie, delenie)