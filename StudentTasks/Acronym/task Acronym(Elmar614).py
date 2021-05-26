# Acronym  Artificial Intelligence
phrase = str(input("Write your full phrase: "))
splited_tex = phrase.split(" ")
shortphrase = " "
for items in splited_tex:
    shortphrase = shortphrase + items[0]
print("Shorted phrase: ", shortphrase)
