# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

a = list()
for i in range(8):
    a.append(input(f"Введите {i+1}-й элемент списка (любое целое число): "))

print(f"Ваш список: {a}")

a = set(a)
print(f"В списке встречается {len(a)} различных чисел.")