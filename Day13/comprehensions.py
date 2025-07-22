# one line  adding
op=[i+2 for i in range(1,10)]
print(op)

op=[x+2 for x in range(1,15)]
print(op)

#square numbers and store in list
op=[x**2 for x in range(1,21)]
print(op)

#upper to change 
str="naveen"
x=str.upper()
print(x)

list=["raj","naveen","ani","kushi"]
op=[x.upper() for i in list]
print(op)

#i want to print square numbers from 10 to 30 only even numbers
op=[x**2 for x in range(10,31) if x%2==0]
print(op)

list1=["hied","hello",'welcome',"something","what","doing"]
op1=[x.upper() for x in list1 if len(x)%2==0]
print(op1)

list1=["hie","hello",'welcome',"something","what","doing"]
def vowelcount(ip):
    count=0
    for x in ip:
        if (x in ['a','e','i','o','u']):
            count+=1
    if (count%2==0):
        return True
    else:
        return False 
op1=[x.upper() for x in list1 if vowelcount(x)]
print(op1)

#perfect number
num=28
sum=0
for i in range(1,num):
    if (num%i==0):
        print(i)
        sum+=i
if (sum==num):
  print("it is a perfect number")
else:
    print("it is not perfect number")



num=55
sum=0
for i in range(1,num):
    if num%i==0:
        print(i)
        sum=sum+i
if sum==num:
    print("it is perfect numbers")
else:
    print("it is not perfect numbers")

num=44
sum=0
for i in range(1,num):
    if num%i==0:
        print(i)
        sum=sum+i
if num==sum:
    print("perfect number")
else:
    print("not perfect number")

num=int(input("enter number:"))
sum=0
for i in range(1,num):
    if num%i==0:
        print(i)
        sum=sum+i
if num==sum:
    print("it is perfect number")
else:
    print("not perfect number")

# num=100
def perfectnumber(num):
    sum=0
    for i in range(1,num):
        if num%2==0:
            print(i)
            sum+=i
    if num%2==0:
        print("perf")
    else:
        print("not")
perfectnumber()


def perfect_number(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            print(i)
            sum+=i
    if num==sum:
        print("perfect")
    else:
        print("not")
perfect_number(28)
perfect_number(30)

# op=[x]
# def sum1(a,b):
#     print(a+b)
# sum1(1,3)
# sum1(22,33)







