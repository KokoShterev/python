# zad 3
import math
a = int(input())
count = 0
while a >= 2:
    a = math.sqrt(a)
    count += 1
print(count)