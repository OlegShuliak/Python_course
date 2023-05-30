# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

import random

n = int(input("Введите длину массива: "))
sp = [random.randint(1, 10) for i in range(n)]
print(sp)

x = int(input("Ведите число Х больше 0: "))
count = x
for i in range(len(sp)):
    if abs(sp[i] - x) <= count and abs(sp[i] - x) != 0:
        count = abs(sp[i] - x)
   
num = set()
for i in range(len(sp)):
    if abs(sp[i] - x) == count:
        num.add(sp[i])

print(f"Ближайшие по величине числа {num}.")