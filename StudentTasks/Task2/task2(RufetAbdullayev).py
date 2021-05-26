dictionary = {
    "Fries" : 10,
    "Sushi" : 15,
    "Pizza" : 13,
    "Taco" : 18
}
d =  {10 : "Fries", 15 : "Sushi", 13 :"Pizza", 18 : "Taco"}
[d.values()]
['Fries', 'Sushi', 'Pizza', 'Taco']
list(d.values())
['Fries', 'Sushi', 'Pizza', 'Taco']
m=[10, 15, 13, 18]
total_price=0
for i in m:
    total_price+=i
if total_price==0 or total_price>35:
        bool = True
        print(bool)
        print('The sum of your menu out of range')

