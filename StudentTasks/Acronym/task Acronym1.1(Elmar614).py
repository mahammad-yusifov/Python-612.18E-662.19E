# Acronym  Ex: Artificial Intelligence(AI), Azerbaijan State Oil and Industry University(ASOIU)
import re
full_phrase = str(input("Write your full phrase: "))
short_phrase = re.sub('[^A-Z]', '', full_phrase)
print("Here is your shorted phrase:", short_phrase)
