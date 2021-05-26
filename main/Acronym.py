# Acronym  Artificial Intelligence - AI, Azerbaijan State Oil Industry University - ASOIU

user_input = str(input("Enter your phrase : "))
txt = user_input.split()
a = " "
for i in txt:
    a = a + str(i[0]).upper()

print("Here is your shortened phrase: ", a)
