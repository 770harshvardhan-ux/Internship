x=((10,20),30,40,["hello","bye"])
print(x,type(x))

for i in x:
    if type(i)==tuple or type(i)==list:
        for j in i:
            print(j)
    else:
        print(i)