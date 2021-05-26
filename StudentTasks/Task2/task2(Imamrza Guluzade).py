dictionary = {
    "levengi" : 20,
    "ash" : 15,
    "xash" : 15
}

print(dictionary)

allPrices = dictionary[("levengi")] + dictionary[("ash")] + dictionary[("xash")]

print("sum of all prices", allPrices)

print(allPrices > 35)