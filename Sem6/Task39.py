# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

def array_in(x):
    return [int(input(f'Введите {i + 1}-й элемент массива: ')) for i in range(x)]

len_a = int(input("Введите длину первого массива: "))
array_a = array_in(len_a)
len_b = int(input("Введите длину второго массива: "))
array_b = array_in(len_b)

print(f'Первый массив: {array_a}')
print(f'Второй массив: {array_b}')

array_res = []
for elem in array_a:
    if elem not in array_b:
        array_res.append(elem)

print(array_res)