# Бонус
# Напишете програма, която при зададен с input стринг цензурира думите, като маха всяка 1ва гласна в думата:
# "Hey my name is Petar" -> "H*y my n*me *s P*tar"

a = input()
b = []
is_first = True
for i in a:
    if i in 'AEIOUaeiou' and is_first == 1:
        b.append('*')
        is_first = False
    elif i == ' ':
        b.append(' ')
        is_first = True
    else:
        b.append(i)
print(''.join(b))
