from clothes import clothes
from grocery import grocery

c=clothes("clothes","jeans",100,799,"black","m")
g=grocery("grocery_section","sugar",60,100,"sugarlite","2026-05-01","2027-05-01")

cart=[]
totalbill=0

while True:
    print("Welcome to dmart\n1.Grocery Section\n2.Clothing Section\n3.exit\n")
    choice=int(input("Enter your choice: \n"))
    match choice:
        case 1:
            print(g.display_grocery_details())

        case 2:
            print(c.display_clothes_details())

        case 3:

            print("1.Buy grocery\n 2.Buy clothes\n")
            ch=int(input("Enter yout choice: "))

            if ch==1:
                qty=int(input("Enter quantity: "))
                amount=qty*g.price
                cart.append(("Sugar",qty,amount))
                totalbill+=amount

            elif ch==2:
                qty=int(input("Enter quantity: "))
                amount=qty*c.price
                cart.append(("Jeans",qty,amount))
                totalbill+=amount

            for item in cart:
                print(f"{item[0]}\t{item[1]}\t{item[2]}")

                print("Total bill: ",totalbill)

        case 4:
            print("THANK YOU!")
            break;

        case _:
            print("Invalid input!")


