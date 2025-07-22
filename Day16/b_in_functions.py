# Day 2/30 – Python Interview Prep Series
# Topic: Tricky Output Questions – Logical & Membership Operators

a="devara"
count=0
for i in a:
    count=count+1
print(count)

#1.type conversion int to float 
#float to int
a=7
b=4.89
print(float(a))   #float
print(int(b))       #integer
print(complex(b))       #complex

#convert  astring "7" to it and multiply it by 5
c="7"
print(int(c)*5)

#converting string to float and add 1
nn="3.1415"
print(float(nn)+1)


#convert tuple to set & dict
t = (4, 5, 6)
print(list(t))     # [4, 5, 6]
print(set(t))      # {4, 5, 6}

# complex
a=20
b=66.8
c="10"
print(complex(a,b))

print(complex(c))
print(dict([('x', 9), ('y', 8)]))  # {'x': 9, 'y': 8}

a=20
b=66.8
c="10"
print(complex(a,b))
print(complex(c))

#absolute
a=int(input("enter number: "))
b=int(input("enter number: "))
c=complex(a,b)
print(abs(c))

#round
a=33.66
b=8.99
c=6.5
print(round(a))
print(round(b))
print(round(c))

#round after digit decimal values
n=6.72489
print(round(n,2))

#round float to int
a=float(input("enter:"))
print(int(round(a)))

# min & max   here zero (02,04) like this are not allowed
tuple1=22,4,35,65,76,22,43,89,0,88
print(max(tuple1))
print(min(tuple1))

#find min and max
num=[2,5,1,9,-3,6]
print(max(num))
print(min(num))

a=30,4,67,
print(max(a))

#11. find alphabetically first name from 
a=["zara","Bob","Alice"]
name=min(a)     #min it mean starting alphabet A
nn=max(a)
print(name)
print(nn)

# power 
a=2
b=5
print(pow(a,b))
# print(pow(a))  # type error

#Get base and exponent from user, return result.
base=int(input("enter base:"))
exponent=int(input("enter component:"))
result=pow(base,exponent)
print(result)

x=2
y=3
z=5
# print((x**y)%z)
print (pow(x,y,z))   #2,3,5=2**3

#divmod
a=9 
b=2
print(divmod(a,b))  #coefficient remainder

c=23
d=5
print(divmod(c,d))

#16. Write function to return quotient and remainder.
def get_quotient_remainder(a,b):
    quotient,remainder=divmod(a,b)
    return quotient,remainder
q,r=get_quotient_remainder(33,4)
print("quotient:",q)
print("remainder:",r)
    
# convert number to binary using repeated divmod(num,2)

# ## absolute  near zero to distance
a=11
b=-8
print(abs(a))
print(abs(a),abs(b))

user=int(input("enter number:"))
print(abs(user))

# 19. Get absolute difference between two numbers.
def absolute_difference(a,b):
    return abs(a-b)
a=33
b=44
print("absolute_difference is :",absolute_difference(a,b))

def manhattan_distance(x,y):
  return abs(x)+abs(y)
x=4
y=7
print("manhattan distance: ",manhattan_distance(x,y))

#21. Multiply two string inputs as integers.
a=input("enter:")
b=input("enter:")
c=int(a)
d=int(b)
print(c*d)

#Round pow (5,3)/7 to 3 decimal values
a=pow(5,3)
print(round(a/7,3))

numbers=[-2,-8,3,7]
largest_abs=max(numbers,key=abs)
print("largest value:",largest_abs)

nn=float(input("enter number:"))
round_num=round(nn)
result=pow(2,round_num)
print(f"2 raised to {round_num} is {result}")



# lst = [1, 2, 3]
# print(str(lst))    # '[1, 2, 3]'
# print(tuple(lst))  # (1, 2, 3)
# print(set(lst))    # {1, 2, 3}
# dict([['a', 1], ['b', 2]])  # {'a': 1, 'b': 2} ✅ (only if list of pairs)


# tuple2=22,4,35,65,76,22,43,89,0,88
# num=5
# for i in tuple2:
#     if num>i:
#         num=i
# print(num)

# tuple2=22,4,35,65,76,22,43,89,0,88
# num=22
# for i in tuple2:
#     if num<i:
#         num=i
#         print(num)





# a='10'
# b=20.8
# print(complex(a))
# print(complex(b))

# a=30,4,67,88,98,78
# print(max(a),min(a))

# a=30,4,67,88,98,78,0
# num=30
# for i in a:
#     if num>i:
#         num=i
# print(num)


