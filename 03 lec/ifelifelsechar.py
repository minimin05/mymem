inchar = input("Input one character ")
if inchar >= 'A' and inchar <= 'Z':
    print("you in put upper case letter ", inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("you in put lower case letter ", inchar)
elif inchar >= '0' and inchar <= '9':
    print("you in put number ", inchar)
else:
    print("It's not a letter or number ", inchar)