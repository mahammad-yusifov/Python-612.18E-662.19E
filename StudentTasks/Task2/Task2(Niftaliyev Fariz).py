# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 11:01:54 2021

@author: fariz
"""
order_numbers = int(input('Please, enter number of orders: '))
meal = input('Enter meal name:')
price = int(input('Enter meal price:'))
meals = {meal: price}
n = 1
total_cost = price
while n < order_numbers:
    meal = input('Enter meal name:')
    price = int(input('Enter meal price:'))
    n += 1
    total_cost = total_cost + price
if n == order_numbers:
    print('Your order was completed!!!')
    print("Total Cost:{}".format(total_cost))
