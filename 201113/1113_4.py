# zad 3
def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):   # only odd numbers
        if n % i == 0:
            return False
    return True

a = int(input())
count = 0
for i in range(2, a + 1):
    if isPrime(i):
        count += i
print(count)