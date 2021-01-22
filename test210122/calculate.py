# Напишете програма, която калкулира приходите за консултантска компания. Компанията приема основно заплащане по 200лв/ден, като има и схема за бонус след отработени определни дни. Схемата за бонусите е следната:
# 0 до 14 дни	 0
# 14 до 30 дни 50лв + основното заплащане
# 30 до 60 дни 80лв + основното заплащане
# над 60 100лв + основното заплащане


def calculate(days):
    if (days <= 14):
        return 200 * days
    elif (days > 14 and days <= 30):
        return days * 200 + 50
    elif (days > 30 and days <= 60):
        return days * 200 + 80
    else:
        return days * 200 + 100
