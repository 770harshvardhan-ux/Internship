g = input("Enter gender(M/F): ")
age = int(input("Enter age: "))
wt = int(input("Enter weight: "))

if (g == "M" and age >= 18 and wt >= 50) or (g == "F" and age >= 20 and wt >= 45):
    print("Selected")
else:
    print("Not selected")
    