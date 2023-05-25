# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# Input 5 -> 1 0 1 1 0
# Output 2

n = int(input("Введите количество монет на столе: "))
up = 0
down = 0

for i in range(n):
    n = int(input("Введите сторону монеты (0 - орел, 1 - решка): "))
    if n == 1:
        up += 1
    else:
        down +=1

minimum = min(up, down)
print(f"Минимальное количество монет, которое можно перевернуть - {minimum}.")



