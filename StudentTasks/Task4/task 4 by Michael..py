# Task4
# given list of unsorted array
# unsortedArray = [7, 4, 9, 22, 31, 4, 1]
# sort this array in reverse order
# use loop to print +2 of all elements inside your sorted array

# hi
MyOwnArray = [18, 29, 77, 111, 228, 1337, 1488, 1111]
MyOwnArray.sort(reverse=True)
print(MyOwnArray)
MyOwnArray.sort(reverse=False)
print(MyOwnArray)
print("MyOwnArray")

for item in MyOwnArray:
    print(item + 2)

# time = 18
# flow = True
# while flow:
#     if time >= 1450:
#         flow = False
#         print("Maximum has been reached")
#     else:
#         time = time + 2
#         print(time)
