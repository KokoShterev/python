# 1. Напишете програма, която калкулира печалба на предприятие. Трябва да има следни компоненти:
# * Функция, която прави калкулацията, връща резултата и извежда на екрана. Приема 3 параметъра: цена за производство, цена на продажба и брой на стоката
# * Взимане на данните от потребителя с input
# Шаблон на функцията:
# def calculate(build_price, sell_price, volume):
#     pass
# Примерни стойности:
# calculate(10,12,100) -> 200
# calculate(32.67, 45, 1200) -> 14796
# calculate(4, 2, 15) -> -30

def calculate(build_price, sell_price, volume):
    return (sell_price - build_price) * volume

build_price, sell_price, volume = map(float, input().split())
print(f'{calculate(build_price, sell_price, volume):.0f}')