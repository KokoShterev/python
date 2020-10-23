for i in range(2000, 5000):
    t = i
    while t > 0:
        n = t % 10
        if n % 2 == 0:
            t //= 10
        else:
            break
    if t == 0:
        print(i, end=",")