# Создать кортеж. Записать в него 10 случайных чисел

import random

numbers = tuple(random.randint(1, 10) for _ in range(10))

print(numbers)
print(type(numbers))

