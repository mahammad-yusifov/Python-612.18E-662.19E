# Random password generator
import random as R
password_len = int(input("Please enter your password's length: "))
elements = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
s = ""
RandomPassword = s.join(R.sample(elements, password_len))
print("Your password is: ", RandomPassword)
