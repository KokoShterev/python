# задача 3
# Напишете програма, която премахва всички числа от списък:
# ["my", 1, "turtle", "explain", 3.14] -> ["my", "turtle", "explain"]

a = ["my", 1, "turtle", "explain", 3.14]
b = [i for i in a if type(i) is not int and type(i) is not float]
# b = list(filter(lambda i: type(i) is not int and type(i) is not float, a))
print(b)
