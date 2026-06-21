num=int(input("Enter vnumber:" ))
sum=0
for i in range(1,num):
    if num%1==0:
        sum+=1

if sum==num:
    print("Perfect number")
else:
    print("Not a perfect number")