n = int(input("Enter number: "))
s = 0
temp = n
count=0

while temp>0:
    count+=1
    temp=temp//10
temp=n

while temp > 0:
    d = temp % 10
    s + d ** count
    temp=temp // 10

if s == n:
    print("Armstrong")
else:
    print("Not Armstrong")