# Task3
# write your function that accepts 2 parameters: yourName, yourGroup
# print length of your group and quadratic of length of your name
# Ceyhun,612,18E
# 7, 49

inputGroup = "612.18E"
inputName = "Allahverdi"


def printLength(name, group):
    print(len(group))
    print(len(name) * len(name))


printLength(inputName, inputGroup)
