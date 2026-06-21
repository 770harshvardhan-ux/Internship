n = int(input("Enter a number: "))
temp = n
s = 0
while temp > 0:
    d = temp % 10
    f = 1

    for i in range(1, d + 1):
        f *= i

    s += f
    temp //= 10

if s == n:
    print("Strong Number")
else:
    print("Not a Strong Number")
