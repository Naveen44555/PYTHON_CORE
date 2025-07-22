# neon - given number and if mutliply that total should be sum is eqaul to given number

num=9
square=num*num
sum=0
while(square>0):
    ld=square%10
    sum+=ld
    square=square//10
if (num==sum):
    print("it is neon")
else:
    print("it is not neon")


num=94
square=num*num
sum=0
while(square>0):
    ld=square%10
    sum=sum+ld
    square=square//10
if(sum==num):
  print("it is neon")
else:
    print('not neon')

#using function
def neon(num):
    square=num*num
    sum=0
    while (square>0):
        ld=square%10
        sum=sum+ld
        square=square//10
    if (sum==num):
        return True
    else:
        return False
op=[x for x in range(1,50) if neon(x)]
print(op)

def neon(num):
    square=num*num
    sum=0
    while (square>0):
        ld=square%10
        sum=sum+ld
        square=square//10
    if sum==num:
        return True
    else:
        return False
op=[x for x in range(1,50) if neon(x)]
print(op)

def neon(num):
    square=num**2
    sum=0
    while(square>0):
        ld=square%10
        sum+=ld
        square=square//10
    if sum==num:
        return True
    else:
        return False
# op=[x for x in range(1,100) if neon(x)]
# print(op)

#tuple
op=tuple(x for x in range(1,100) if neon(x))
print(op)

op={x for x in range(1,100) if neon(x)}
print(op)



#  # perfect square

# num=16
# isperfect=False
# for x in range(1,num):
#     if (x**2==num):
#         isperfect=True
#         break
# if (isperfect):
#     print("it is perfect square")
# else:
#     print("not")

# num=44
# is_perfect=False
# for i in range(1,num):
#     if (i**2==num):
#         is_perfect=True
#         break
# if(is_perfect):
#     print(num,"it is perfect square")
# else:
#     print(num,"not perfect") 

# #sunny number
# num=24
# is_sunny=False
# for i in range(1,num):
#     if (i**2==num+1):
#         is_sunny=True
#         break 
# if (is_sunny):
#     print("it is sunny number ")
# else:
#     print("it is not sunny number")


num=int(input("enter number:"))
if num>1:
    for i in range(1,num):
        if num%i==0:
            print("it is not prime")
        else:
            print(i,"prime")
else:
    print('not prime')


#prime number
num=22
isprime=True
if num<=1:
    print("please give number greater than 1")
else:
    for i in range(2,num):
        if num%2==0:
            print("not prime number")
            isprime=False
            break
    if (isprime):
        print("it is prime number")
    else:
        print("not prime number")


def num(prime):
    num=33


num=["naveen","raj"]
for i in num:
    for x in i:
        print(x)

ip=["hii","hello","where"]
for x in ip:
  rev=""
  for i in range(len(x) -1,-1,-1):
    rev+=x[i]
  print(rev)


#sunny number
num=24
is_sunny=False
for i in range(1,num):
    if (i**2==num+1):
        is_sunny=True
        break 
if (is_sunny):
    print("it is sunny number ")
else:
    print("it is not sunny number")

#neon number
num=0
square=num*num
value=str(square)#'100'
count=0
for x in value:
    count+=int(x)
if num==count:
    print("neon")
else:
    print("not a neon")


#neon number using function

def neon(num):
    square=num*num
    value=str(square)#'100'
    count=0
    for x in value:
        count+=int(x)
    if num==count:
        return True
    else:
        return False
result=[x for x in range(1,100) if neon(x)]
print(result)

#perfect square
num=81
is_perfect=False
for i in range(1,10):
    sum1=i*i
    if sum1==num:
      is_perfect=True
      print(f"it is perfect square for {i}")
      break
else:
     is_perfect=False
     print("not perfect square")

     

#perfect square
num=80
is_perfect=False
for i in range(1,10):
    sum1=i*i
    if sum1==num+1:
      is_perfect=True
      print("it is neon number ")
      break
else:
     is_perfect=False
     print("not not neon number")

num=49
is_perfect=False
for i in range(1,num):
    sum1=i*i
    if num==sum:
        is_perfect=True
        print(i,"it is perfect square")
        break
else:
    is_perfect=False




