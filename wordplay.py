first = input("Enter first word: ")
second = input("Enter second word: ")
choice = input("Select (c)oncat, (s)wap, (r)everse: ")

def reverse (string):
    return string[::-1]

if choice == "c":
    print(first + " " + second)

elif choice == "s":
    print(second + " " + first)

elif choice == "r":
    print(reverse(first + " " + second))

else:
    print("Incorrect entry, please try again")
