# zad 1
str = input()
str1=[]
for i in str:
    if i.lower() in 'aeiouаъоуеиюя':
        str1.append(i*4)
    else:
        str1.append(i)
print(''.join(str1))