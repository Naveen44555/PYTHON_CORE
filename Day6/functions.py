# functions
def func():
    print("This is function")
func()

def add(a,b):
    print(a+b)
add(3,4)

#function with in function
def outer():
    print("this is outer")
    def inner():
        print("this is inner")
    inner()
outer()

# Positional arguments

def naveen(a,b):
 print(a,b)
naveen("nn","uu")

def det(name,pin):
    print(name)                    #print(name,pin)
    print(pin)
det("naveen","909")
 
#keyword arguments

def det(name,pin):
    print(name,pin)
det(pin=909,name="naveen")

def details(a,b): 
    print(a)
    print(b)
details(b="naveen",a="vinay")

def details (name,age,pn,ad,em,bg) :
 print(f"name is {name}")
 print(f"age is {age}")  
 print(f"pn is {pn}")
 print(f"ad is {ad}")
 print(f"em is {em}")
 print(f"bg is {bg}")
details(name="honey",age="2",pn=8186077704,ad="annaram",em="jani@gmail.com",bg="o+")

# default argument
def details(a,b,c="anii"):
    print(a)
    print(b)
    print(c)
details("kushi","op")

# addition & subtraction
def add():
    a=53
    b=10000
    print(a+b)
add()
#                  #method - 2
def add(a,b):  
    print(a+b)
add(3,5)

def add(a,b):
    print(a+b)
add(6,4)

def sub(c,d):
    e=c+d     # or directly print(c+d)
    print(e)
sub(7,8)

#    return 

def function_name():
    return "nn"
print(function_name())

def naveen():
    return "hi how are you"
print(naveen())

#return  and using operator
def sub(a,b):
  sub=a-b
  return sub
print(sub(5,2))
 
def add(a,b):
    add=a+b
    return add
print(add(4,6))

def div(a,b):
    div=a/b
    return div
print(div(7,6))

def mul(a,b):
   mul=a*b
   return mul
print(mul(3,4))

def add(a,b):
    add=a+b
    return add
print(add(4,6))

def naveen(student='honey',branch='civil'):
 print(f"welcome {student},hope you do good in {branch} program")
naveen()
   
def naveen(a,b):
    naveen=a-b
    return naveen
print(naveen(4,2))

# using f string
# method 1

def naveen():
    name=input("enter your name:")
    age=int(input("enter your age "))
    print(f"your name is {name},and your age is {age + 10} in 2035")
naveen()

 #method 2
def naveen(a,b):
   print(f"welcome {a} hope you good in your {b} program.")
a=input("enter your name: ")
b=input("enter your branch: ")
naveen(a,b)

##method 3
def naveen(a,b):
    return "nice"
a=input("enter your name")
b=input("enter your branch")
print(f"welcome {a} hope you good in your {b} program.")
naveen("raju","mechanical")
   
def naveen(a="raj",branch="civil"):
 print(f"hi {a},you are {branch}")
naveen("kiran","mechanical")
    
def even(a):
    if a%2==0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")
even(3)

def add(*numbers):
    print(sum(numbers))
add(11,2,344,4)

def add(*numbers):
    print(len(numbers))
    print(sum(numbers))
add(11,2,344,4)

def details(*detail,batch=53):
    print(batch)
    print(detail)
details("naveen","10","Dcl")