# Сгенерируйте список случайных чисел от 1 до 20, состоящий
# из 10 элементов. Удалите из списка дубликаты уже имеющихся элементов.
# Определите, сколько элементов было удалено.

import random
numbers = [random.randint(1, 20) for _ in range(10)]
print(numbers)
length = len(numbers)
numbers = list(set(numbers))
print(numbers)
print(f'Элементов было удалено: {length - len(numbers)}')