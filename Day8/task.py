# 1.check even or odd
a=int(input("enter number: "))
if a%2==0:
    print(f"{a} is even number")
else:
    print("odd")

# 2.divisible by 5 but not by 10
num=int(input("enter a number: "))
if(num%5==0 and num%10!=0):
    print("satisy")
else:
    print("not satisfy")
    
#3.Biggest Among two numbers
A=4
B=7
if A>B:
 print("A is biggest")
else:
 print(f"Biggest is:{B}")

#4.smallest Among two Numbers
x=4
y=7
if x<y:
    print(f"smallest is {x}")
else:
    print(f"smallest is {y}")
    
#5.Divisible by 2,3,and 6
number=int(input("enter a number: "))
if (number%2==0 and number%3==0 and number%6==0):
    print(f"satisfy,{number} is divisible by 2,3and 6")
else:
    print("it is not divisible by 2,3 and 6")
#both 12,18 and 24 are divisible by 2,3 and 6

#6.voting Eligibility
age=int(input("enter a number:"))
if age>=18:
    print("you are eligible to vote")
else:
    print("not eligible to vote")

# 7.student Pass/Fail based any subjects>=35
maths=40
physics=38
chemistry=30
if(maths>=35 and physics>=35 and chemistry>=30):
    print("pass")
else:
    print("fail")
    
#8.student pass if passed any subject(>=35)
m=20
p=38
ch=25
if (m>=35 or p>=35 or ch>=35):
    print("pass")
else:
    print("fail")

#9.student pass if passed any two subjects
m=40
p=20
ch=36
if(m>=35 and p>=35) or( m>=35 and ch>=35)or (p>=35 and ch>=35):
    print("pass")
else:
    print("fail")

#10. biggest Among three numbers
a=input("enter a number")
b=input("enter b number")
c=input("enter c number")
if (a>b and a>c):
    print(f"biggest is {a}")
elif (b>c):
    print(f"biggest is{b}")
else:
    print(f"biggest is : {c}")

# 11.smallest among three numbers
x=input("enter a number")
y=input("enter y number")
z=input("enter z number")
if x<y and x<z:
    print(f"{x} is smallest")
elif y<z:
    print(f"{y} is smallest")
else:
    print(f"{z} is smallest")

# 12.perfect squae or not
a=int(input("enter a number:"))
if a**2 :
    print(f"perfect square{a}")
else:
    print("it is not perfect square")

a=35
b=a**0.5
print((b))
if b==int(b):
    print("perfect sq")
else:
    print("not sq")

#13.cars required for members
import math
members=int(input("enter a number:"))
cars=members/5
# print(ceil.round(cars))

#13.cars required for members
members=int(input("enter a number:"))
cars=(members+4)//5
print(f" {cars} cars is needed")

# method-2
members=int(input("enter a number:"))
if members%5==0:
    cars=members//5
else:
    cars=(members//5)+1
print(cars)

#14.second biggest among three numbers
a=int(input("enter a number:"))
b=int(input("enter b number:"))
c=int(input("enter c number:"))
if (a>b and a<c)or (a>c and a<b):
    print("a is")
elif (b<a and b>c):
    print("d")
else:
    print("gg")
    
a=int(input("enter a number:"))
b=int(input("enter b number:"))
c=int(input("enter c number:"))
# if a>b and a<c or 
    