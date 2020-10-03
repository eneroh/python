while True:
	x = float(input("first number: "))
	op = input("Operation: ")
	y = float(input("second number: "))

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
