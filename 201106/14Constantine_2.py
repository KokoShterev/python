# задача 2
# Напишете програма, която при зададен string преброява гласните(бонус ако е за кирилица):
# "effect" -> 2
# "course" -> 3
# ** y не е гласна

a = input()
count = 0
for i in a:
    if i.lower() in 'aeiouаъоуеиюя':
        count += 1
print(count)
