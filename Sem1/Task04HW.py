# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

s = int(input("Введите количество сделанных журавликов: "))

if s % 6 == 0:
    print(f"Петя сделал {s // 6} журавликов.")
    print(f"Катя сделала {s // 6 * 4} журавликов.")
    print(f"Сережа сделал {s // 6} журавликов.")
else:
    print("Столько целых журавликов сделать невозможно:)")