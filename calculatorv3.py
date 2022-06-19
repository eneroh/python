#!/bin/python

def add(x,y):
	return x + y

def subtract(x,y):
	return x - y

def multiply(x,y):
	return x * y

def divide(x,y):
	return x / y

while True:
	print("Pick your operation.")
	print("1. Add")
	print("2. Subtract")
	print("3. Multiply")
	print("4. Divide")
	op = input("Operation(1,2,3,4): ")

	if op in ('1','2','3','4'):
		x = float(input("first number: "))
		y = float(input("second number: "))
		
		if op == "1":
			print(x, "+", y, "=", add(x,y))

		elif op == "2":
			print(x, "-", y, "=", subtract(x,y))

		elif op == "3":
			print(x, "*", y, "=", multiply(x,y))
		elif op == "4":
			print(x, "/", y, "=", divide(x,y))
		break
	else:
		print("Error, please try again")
	print(exit)

based on https://www.programiz.com/python-programming/examples/calculator
