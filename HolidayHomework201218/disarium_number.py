# 2. Напишете функция, която проверява приема 1 число и проверява дали е Disarium. Всяка от цифрите вдигнати на степен спрямо позицията им (от ляво на дясно) трябва да е равна на числото. Тоест:
# 135 - 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135 - True
# 89 - 8^1 + 9^2 = 8 + 81 = 89 True
# 13 - 1^1 + 3^2 = 10 False

def disarium_number(a):
    digits = 0
    sum = 0
    t = a
    while t:
        t = t // 10
        digits += 1
    t = a
    while digits:
        sum += (t % 10) ** digits
        t = t // 10
        digits -= 1
    if sum == a:
        return True
    return False

print(disarium_number(175))