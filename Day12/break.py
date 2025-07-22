for i in range(1,10):
    print(i)
    if i==5:
        break

for x in range(1,10):
    if x==5:
        break
    print(x)


# reverse print
x="ollo"
op=""
for chr in range(len(x)-1,-1,-1):
    op+=x[chr]
print(op)


if (op==x):
    print("it is palindrome")
else:
    print("it is not palindrome")

str="hello"
op=""
for i in range(len(str)-1,-1,-1):
    op+=str[i]
print(op)


naveen="yadav"
op=""
for x in range(len(naveen)-1,-1,-1):
    op+=naveen[x]
print(op)

str="2345"
op=""
for i in range(len(str)-1,-1,-1):
    op+=str[i]
print(op)

x=input("enter a string")
str=""
y=len(x)-1
while y>=0:
    str+=x[y]
    y=1
    
string="racecar1"
op=""
for i in range(len(string)-1,-1,-1):
    op+=string[i]
print(op)

string="racecar1"
op=""
while i in string:
    print(i)
    