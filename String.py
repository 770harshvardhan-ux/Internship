"""name="ram"
print(name)
#return index char
print(name[0])
#return memory reference
print(id(name))

new_name="p"+name[1:3]
print(name[1:3])
print(new_name)"""


"""str="Maharashtra"

print(str[0:4])
print(str[6:10])
#even index
print(str[::2])
#last character
print(str[-1])
#reverse
print(str[::-1])"""

"""str="Maharashtra"

for i in range(len(str)):
    if i % 2 != 0:
        print(str[i], end="")

for ch in str:
    if ch in "aeiouAEIOU":
        print(ch)

even=0
odd=0
for i in range(len(str)):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Even characters: ",even)
print("Odd characters: ",odd)    

s="hello"
rev=""
for ch in s:
    rev=ch+rev
print(rev)"""
