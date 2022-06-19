#!/bin/python                                                                                         

"""
alcohol.py

Well, now I'm just doing a basic logical/conditional statement.

Let's see how this plays out
"""

age = input("Please input your age: ")
money = input("Please input your money: ")

def alcohol(age,money):

    if (age >= str(21)) and (money >= str(5)):
        return "Drink responsibly ;)"
    elif (age >= str(21)) and (money < str(5)):
        return "Man, get yo money in check"
    elif (age < str(21)) and (money >= str(5)):
        return "Listen son, you need jesus!"
    else:
        return "Invald entry, please try again!"

print(alcohol(age,money))
