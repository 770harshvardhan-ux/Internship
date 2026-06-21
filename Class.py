"""Program 1
a=10
b=20
a+=b
print(a)
b+=a
b*=2
print(b)
a/-2
b%-a
print(a+b)"""


"""Program 2
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("Addition- ",(num1+num2))"""


"""Program 3
num1=int(input("Enter number: "))

if num1 % 2 == 0:
    print("Number is even.")
else:
    print("Number is odd.")"""


"""Program 4
username=input("Enter username: ")
password=input("Enter password: ")
if username =="admin":
    if password=="admin123":
        print("Login successful!")
    else:
        print("Incorrect password")
else:
    print("Username not found")"""

"""Program 5
units=int(input("Enter units: "))

if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 100 * 2 + (units - 100) * 3
else:
    bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    print(bill)"""


"""Program 6
print("---Calculator---\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n")

choice=int(input("Enter your choice: "))

match choice:
    case 1:
        num1=int(input("Enter first number: \n"))
        num2=int(input("Enter second numner: \n"))
        print("Addition of" ,  num1, "and", num2, "is:",num1+num2)
    case 2:
        num1=int(input("Enter first number: \n"))
        num2=int(input("Enter second numner: \n"))
        print("Subtraction of" , num1, "and" , num2, "is:" ,num1-num2)
    case 3:
        num1=int(input("Enter first number: \n"))
        num2=int(input("Enter second numner: \n"))
        print("Multiplication of" , num1, "and" , num2, "is:" ,num1*num2)
    case 4:
        num1=int(input("Enter first number: \n"))
        num2=int(input("Enter second numner: \n"))
        print("Division of" , num1, "and" , num2, "is:" ,num1/num2)
    case _:
        print("Invalid choice!")"""


""" Program 7
choice=int(input("Enter your choice: "))

match choice:
    case 1|2|3|4|5:
        print("Weekday")
    case 6|7:
        print("Weekend") """   


"""Program 8
i=1
sum=0
while i<=10:
    sum=sum+i
    i+=1

print(sum)"""

"""Program 9
i=26
while i>15:
    i-=1
    print(i)"""

"""Program 10
i=10
while i<=20:
    print(i,"- Square = ",i*i)
    i+=1"""

"""Program 11
i=1
sum=0
while i<=50:
    if i % 2 == 0:
        sum=sum+i
    i+=1
print("Sum= ",sum)"""

"""Program 12
i=0
while i<5:
    i+=1
    if i==4:
        continue
    print(i)"""





