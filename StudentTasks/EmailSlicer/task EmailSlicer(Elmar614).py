# email slicer
mail = str(input("Write email : "))
username = mail.split("@")[0]
domain = mail.split("@")[1]
print("Your username is :", username, "and your domain is :", domain)
