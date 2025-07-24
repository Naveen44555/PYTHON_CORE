# def add():
#     a=33
#     b=44
#     print(a+b)
# add()

# #default arguments
# def default (name,class1,a="naveen" ):
#     print(name)
#     print(class1)
#     print(a)
# default('nave',53)

# def table(number,end=10):
#     for i in range(1,end+1):
#         print(f"{number}*{i}={number*i}")
# table(2,4)

# def table(number,end=10):
#     for i in range(1,end+1):
#         print(f"{number}*{i}={number*i}")
# table(3)

# for i in range(1,11):
#     print(f"2*{i}={2*i}")

# table=int(input("number:"))
# for i in range(1,11):
#     print(f"{table}*{i}={table*i}")


# #keyword arguments
# def details(pin,name):
#     print(name,pin)
# details(pin=99,name="naveen")

#arbitary arguments
def class1(*name):
    print(name)
class1(3.4,5,"naveen")

#kwarbitary arguments
def details(**detail):
    print(detail)
details(n="44R3",d=45,b=456,bn=456,kk=456,)

def details(n,b):
    return n+b
print(details(3,5))




# #default
# def greet(b,name="nn"):
#     print(b,f"hello,{name}!")
# greet("naveen")



# #postional arguments
# # def add1 ()

# num=int(input("enter :"))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#         print("prime")
# else:
#   print("invalid")

# chr="naveen"
# vowels=["a","e","i","o","u"]
# temp=[]
# for i in chr:
#     if i in vowels:
#         temp.append(i)
# print(temp)
   
