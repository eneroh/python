first = input("Enter first word: ")
second = input("Enter second word: ")
selection = input("select (c)oncat, (s)wap, (r)everse")

def reverse (string):
    return string[::-1]

if selection == "c":
    print(first + " " + second)

elif selection == "s":
    print(second + " " + first)

elif selection == "r":
    print(reverse(first + " " + second))

else:
    print("please try again")
