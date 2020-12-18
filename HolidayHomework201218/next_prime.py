# 1. Напишете функция, която приема 1 параметър и връща следващото просто число:
# next_prime(12) -> 13
# next_prime(24) -> 29
# Ако подаденото число е просто го връщате него

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def next_prime(a):
    while True:
        if is_prime(a):
            return a
        a += 1

number = int(input("Input your number: "))
print (f'The next prime is {next_prime(number)}')