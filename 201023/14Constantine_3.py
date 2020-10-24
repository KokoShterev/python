a = input()
d = 0
ch = 0
for i in a:
    if i.isdigit():
        d += 1
    elif i.isalpha():
        ch += 1
print("{} digit/s and {} char/s".format(d, ch))