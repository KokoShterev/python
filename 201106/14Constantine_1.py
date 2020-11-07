# задача 1
# Имате зададени 2 числа num и count - като трябва да изведете count на брой кратни числа  на числото num. Пример:
# 3, 5 -> 3, 6, 9, 12, 15
# 4, 2 -> 4, 8

str = input()
num, count = map(int, str.split())
for i in range(1, count + 1):
    print(f'{num * i}', end=' ')
