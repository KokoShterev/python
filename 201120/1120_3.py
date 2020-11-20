def my_f(a):
    count = 0
    while a >= 2:
        a = a**0.5
        count += 1
    return count
a = int(input())
print(my_f(a))