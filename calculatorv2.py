while True:
	x = int(input("first number: "))
	op = input("Operation(+,-,*,/): ")
	y = int(input("second number: "))

	if op == "+":
		print(x + y)
	elif op == "-":
		print(x - y)
	elif op == "*":
		print(x * y)

	elif op == "/":
		print(x / y)
	else:
		print("Error, please try again")	
	print(exit)
