liked = '(Wanted Meal)'
unliked = '(Unwanted Meal)'
dictionary = {
    "Burger": 5,
    "Fish" : 18,
    "Barbecue": 30,
    "Pizza": 55,

}
print (dictionary[("Pizza")], 'is a price of my favorite food')
FavoriteFood1 = dictionary ["Barbecue"]

if (FavoriteFood1>35):
    print (True, liked)
else:
    print (False, unliked)

print ('We should try another time.')
FavoriteFood = dictionary ["Pizza"]
if (FavoriteFood>35):
    print (True, liked)
else:
    print (False, unliked)
