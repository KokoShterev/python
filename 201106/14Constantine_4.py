# задача 4
# Напишете програма, която проверява дали дадено число взето с input е симетрично:
# 4334 -> True
# 347 -> False

a = input()
b = a[::-1]
print('True') if a == b else print('False')
