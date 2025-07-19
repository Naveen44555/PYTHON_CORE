# check even or odd number
number=int(input("enter a number to check it is even or odd:"))
if(number%2==0):
    print("it is even number")
else :
    print(f"you enterd {number} it is odd number")
print("bye....")


#check numbers is positive or negative zero
num=int(input("enter a number:"))
if num<0:
    print("negative")
elif num>0:
    print("positive ")
elif num==0:
    print("zero")
else:
    print('nothing')
    
# here you can see you are a kid or young etc....

Age=int(input("enter your age: "))
if(Age<=12):
    print(f" your age is {Age} you are kid")
elif(Age<=19):
    print(f"your age is {Age} you are teenager" )
elif(Age<=40):
    print(f" your age is {Age} you are younger boy")
elif(Age<=59):
    print(f" your age is {Age} you are Prime")
else:
     print(f" your age is {Age} you are senior")

T=int(input('enter your marks'))
H=int(input('enter your marks'))
E=int(input('enter your marks'))
M=int(input('enter your marks'))
P=int(input('enter your marks'))
S=int(input('enter your marks'))
total_marks=T+H+E+M+P+S
percentage=(total_marks/600)*100
if(percentage>=90):
    print("you got A grade")
elif(percentage>=80):
    print("you got B grade")
elif(percentage>=70):
    print("you are C grade")
elif(percentage>=60):    
    print("you got D grade")
elif(percentage<=59):    
    print("you got D grade")
else:
    print("you got F grade & fail")

# traingle type check

a=int(input("enter a number"))
b=int(input("enter b number"))
c=int(input("enter c number"))
if(a==b==c):
    print("equilateral")
elif(a==b or b==c or c==a):
    print("isosceles")
elif(a!=b!=c):
    print("scalene")
else:
    print("it is not triangle")
    
#balance check

available_balance=int(input("enter curently balance:"))
withdrawan=int(input("enter money to withdrawan:"))
if(available_balance>withdrawan):
    if(withdrawan%100==0):
        print(f"your amount {withdrawan} is successfully withdrawan")
    else:
        print("only muliples of 100's are withdrawan")
else:
    print("insufficient balance")