def wash_hands(n, months):
    all_sec = n * months * 30 * 21
    min = all_sec // 60
    sec = all_sec - (min * 60)
    return min, sec
n, months = map(int, input().split())
min, sec = wash_hands(n, months)
print(f'{min} минути и {sec} секунди')