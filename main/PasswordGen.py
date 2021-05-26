# password generator
import random

passlen = int(input("Enter the length of password: "))
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
s = ""
generatedPassword = s.join(random.sample(characters, passlen))
print("here is your password: ", generatedPassword)
