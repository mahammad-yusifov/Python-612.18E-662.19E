desired = '(Desired Meal)'
undesired = '(Undesired Meal)'
dictionary = {
    "kinder": 2,
    "rice" : 4,
    "Lobster": 20,
    "Irish fish": 55,

}
print (dictionary[("Irish fish")], 'is a price of my favorite food')
FavoriteFood1 = dictionary ["Lobster"]

if (FavoriteFood1>35):
    print (True, desired)
else:
    print (False, undesired)

print ('We should take another attempt to calculate the price of favorite food')
FavoriteFood = dictionary ["Irish fish"]
if (FavoriteFood>35):
    print (True, desired)
else:
    print (False, undesired)
