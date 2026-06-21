"""list=[10,20,30]
print(type(list))
print(list)
print(list[1])
list[1]=50
print(list)

print(len(list))
print(sum(list))
print(max(list))"""

"""x=[]
no=int(input("Enter any number: "))
x.append(no)
print(x)"""

"""x=[10,20,30,40]
sum=0
for i in x:
    sq=i*i
    print(sq)
    sum=sum+sq
    print(sum)"""

"""x=[21,32,65,24,5]
for i in range(len(x)):
    if x[i]%2==0:
        x[i]=0
    else:
        x[i]=1
print(x)"""


"""x=[[1,"Car",500],
   [2,"Doll",1000],
   [3,"Grocery",2000],
   [4,"Sunglasses",3000]]

print(x,type(x))

for ids in x:
    print(ids[2])

x[2][2]=2500
print(X)"""

"""n=int(input("Enter the number of elements: "))

list=[]
for i in range(n):
    x=input("Enter element: ")
    list.append(x)

print(list)"""


#n=int(input("Enter the number of elements: "))

"""list=[]

for i in range(n):
    no=int(input("Enter Product ID: "))
    name=input("Enter Product name: ")
    price=int(input("Enter the price of product: "))

    list.append([no,name,price])
print(list)"""

#view add update delete buy search

n=int(input("Enter the number of products: "))

products=[]

for i in range(n):
    pid=int(input("Enter product ID: "))
    name=input("Enter product name: ")
    price=int(input("Enter product price: "))

    products.append([pid,name,price])

while True:
    print("\n----- MENU -----")
    print("1. View Products")
    print("2. Add Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Buy Product")
    print("6. Search Product")
    print("7. Exit")

    ch=int(input("Enter your choice: "))

    if ch==1:
        print("\nProduct list")
        for p in products:
            print(p)

    elif ch==2:
        pid=int(input("Enter Product ID: "))
        name=input("Enter Product name: ")
        price=int(input("Enter the price of Product: "))

        products.append([pid,name,price])
        print("Product added successfully!")

    elif ch==3:
        pid=int(input("Enter Product ID to update: "))

        for p in products:
            if p[0]==pid:
                p[1]=input("Enter new name: ")
                p[2]=int(input("Enter new price: "))
                print("Product updated successfully")
                break

            else:
                print("Product not found")

    elif ch==4:
        print("1. Delete specific product")
        print("2. Delete all products")

        d=int(input("Enter choice: "))

        if d==1:
            pid=int(input("Enter product id to delete: "))

            for p in products:
                if p[0]==pid:
                    products.remove(p)
                    print("Product deleted successfully")
                    break
                else:
                    print("Product not found")

        elif d==2:
            products.clear()
            print("All products deleted")

    elif ch==5:
        pid=int(input("Enter product id to buy: "))

        for p in products:
            if p[0]==pid:
                qty=int(input("Enter quantity: "))
                total=p[2]*qty

                print("Product name: ",p[1])
                print("Price       : ",p[2])
                print("Quantity    : ",qty)
                print("Total amount: ",total)
                break
            else:
                print("Product not found")

    elif ch==6:
        pid=int(input("Enter product id to search: "))

        for p in products:
            if p[0]==pid:
                print("Product found")
                print(p)
                break
            else:
                print("Product not found")

    elif ch==7:
        print("Program ended")
        break

    else:
        print("Invalid choice")
