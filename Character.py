ch = input("Enter character: ")

if ch.isupper():
    print("Character is capital")
elif ch.islower():
    print("Character is lower")
elif ch.isdigit():
    print("Character is digit")
else:
    print("Chracter is other symbol")

