# task 1
# download python and ide
# display your name and surname
# print the multipilication of your age and number of characters you have in your name and surname
# shift + f10 - run shortcut

# compiler (java) - intrepreter (python) matlab ruby
# .exe C# C++      .py
# .jar .exe .java  .py

# String, Integer, FLoat, Boolean, List, Dictionary
# "jett"
# "6"
# "3.14"
# True, False
# ["s", "a", "l","a","m"]
# [
# "name" : "Ayten"
#  "surname" : ""
# ]
# 5  str(5) = "5"
# 4  int("4") = 4

# dictionary = {
#     "Imamrza" : 10,
#     "Lacin" : 11,
#     "Ceyhun" : 12
#  }
#
# print(dictionary[("Ceyhun")])

# task 2
# Create Dictionary containing your favourite meals and prices
# If price of your most favourite meal is higher than 35 print true

# built-in functions
# camel-case, snake-case
# myVariableOne my_variable_one

# argument, parameter
# pinMode(2,OUTPUT)

# ctrl alt l
# Null - empty, 0, nothing, None

#
#
# def sum_val(*values):
#     print(values[3])
#
#
# sum_val(4, 5, 7, 2, 1)

# sorting placing smallest to the highest

# Task3
# write your function that accepts 2 parameters: yourName, yourGroup
# print length of your group and quadratic of length of your name
# Ceyhun,612,18E
# 7, 49

# list = [7, 92, 12, 77, 2]
# # list.sort(reverse=False)
# list.sort()
# # list.reverse()
# list = list[::-1]
# print(list)
# num = 1
# run = True
# while run:
#     if num == 50:
#         run = False
#         print("Reached 50")
#     else:
#         print(num)
#         num = num +1

# Iteration - loop
# Recursion- function cals itself

# Task4
# given list of unsorted array
# unsortedArray = [7, 4, 9, 22, 31, 4, 1]
# sort this array in reverse order
# use loop to print +2 of all elements inside your sorted array


# Task5
# Calculator
# Build from beginning and rename function,parameter names

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


print("Welcome to Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
select = int(input("Select Operation: "))

if select > 4:
    print("invalid operation")
    exit()

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
          add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
          subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
          multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
          divide(number_1, number_2))
else:
    print("Not supported yet")
