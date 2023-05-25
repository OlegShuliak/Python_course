# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

n = int(input("Введите любое целое положительное число больше 0: "))
pow2 = 1
pow_res = 0
pow_str = str("1")

while pow_res < n:
    pow_res = 2 ** pow2
    pow2 += 1
    if  pow_res < n:
        pow_str += ", " + str(pow_res)
    elif pow_res == n:
        pow_str += ", " + str(pow_res) + "."
    else:
        pow_str += "."

print(f"Все целые степени двойки: {pow_str}")
