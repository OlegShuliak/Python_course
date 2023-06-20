# Создайте кортеж, заполненный случайными числами.
# Напишите метод, который заменыет элемент в кортеже
# по заданному индексу другим случайным числом.

def change_element(numbers, index):
    return numbers[:index] + (random.randint(1, 100), ) + numbers[index + 1:]

import random
numbers = tuple(random.randint(1, 100) for _ in range(10))
index = 4

print(numbers)
numbers = change_element(numbers, index)
print(numbers)
