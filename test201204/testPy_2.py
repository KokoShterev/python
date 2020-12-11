# Според проучванията трябват 21 секунди да се мият ръцете, за да се премахне Covid вируса от тях. Напишете програма, която калкулира колко време
# отделяме за това занимание. Програмата трябва да има:
# * Функция, която прави калкулацията, връща резултата и извежда на екрана. Приема 2 параметъра: колко пъти на ден мием ръцете и колко месеца го изпълняваме.
# * Изведената информация трябва да е в МИНУТИ
# Приемете, че всеки месец е с 30 дни
# Шаблон на функцията
# def wash_hands(n, months):
#     pass
# Примерни стойности:
# wash_hands(5, 2) -> 105 минути и 0 секунди
# wash_hands(8, 7) -> 588 минути и 0 секунди

def wash_hands(n, months):
    all_sec = n * months * 30 * 21
    min = all_sec // 60
    sec = all_sec % 60
    return min, sec
n, months = map(int, input().split())
min, sec = wash_hands(n, months)
print(f'{min} минути и {sec} секунди')