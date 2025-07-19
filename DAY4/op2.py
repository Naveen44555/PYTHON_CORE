#operators
# arithmetic operator
a=7           #addition 
b=6
print(a+b)

c=7         #subtraction
d=9
print(d-c)
#a=a-6 (or)a-=6
m=7         #multiply
n=5
print(m*n)

R=8         #divison
s=3         #float values
R=R/s
print(R)

m=5        #floor divison
n=2
print(m//n)

s=7         #modulus
t=2
remainder=s%t
print(remainder)
n=5         #exponential
p=2
print(n**p)

print(5+2*3-1+10/5)

#Assignment operator
P=6     # =Assignment
a=8         # +=add and assign
b=5
a=a+b  #a+=b
print(a)

a=6     # -= sub and assign
b=5
a-=b  #a=a-b
print(a)

c=6     #*= multiply and assign
d=5
c*=b  
print(c)
c=6     # /= divison and assign
d=5
c=c/b  
print(c)

c=6     # //= floor divison and assign
d=5
c=c//b  
print(c)
v=8     # %=modulus and assign
b=3
print(v%b)

b=7     # **= exponentiate and assign
v=3
v=b**v
print(v)

#comparision operator
s=4     #equal to 
d=4         #True or false
print(s==d)
m=6     #not equal to
n=7
print((m+5)!=n)
print(m==n)

quantity_in_store=25
client_require=35
print(quantity_in_store>client_require) 
print(quantity_in_store<client_require) 

#    > and <  
str1="welcome"
str2="something"
print(len(str1)>len(str2))
print(10>=10) 
print(10<=8) 

#logical operators
a=5         #and
c=6
print(8<c and a>3)

a=True     #or
b=False
c= a or b
print(c)
a=True      #not
b=False
c= not b
print(c)

a=5
b=3
print(True and False) 
print(a>2 and b>5) 
print(True or False) 
print(a>2 or b>5) 
print(True and True)
print(True or True) 
print(a<10 and b<5) 
print(False and False)
print(False or False) 
print(a>10 and b>5) 
print(False and True)
print(False or True)
print(not False)

# membership operator
t=[1,2,4,5]     #in
print(2 in t)
v="Naveen"         # not in 
print('N' not in v)

fruits=['apple','grapes','banana','watermelon']
is_apple_the_list='apple'in fruits
print("'apple' in the fruits:",is_apple_the_list)

fruits=['apple','grapes','banana','lemon']
is_watermelon_not_in_the_list='water melon' not in fruits
print("'water melon' not in the fruits:",is_watermelon_not_in_the_list)

#identity operator
name1="naveen"      #is
name2="naveen"
result_is="name1 is name2"
print(name1 is name2,result_is)

num1=20           #isnot
num2=40
print(num1 is not num2)

# bitwise operator
a=5                 
b=6
print(a&b) #&
print(a|b)  #or
print(a^b)  #xor
print(~a)   #~not (compliment)
print(a<<2) #left shift
print(a>>2) #t right shift

a=26
b=23
print(a&b)

a=17
b=24
print(a|b)

a=45
print(~45)

a=68
print(68<<2)
a=56
print(56>>3)

weight=input('enter your weight in kilogram:')
height=input('enter your height in centimeter:')
bmi=int(weight)/float(height)
print(int(bmi))
             
print(round(11.5))
print(round(467,-3))

# 1.simple interest formula ptr/100
price=int(input("enter price:" ))
time=int(input("enter time in months: "))
rate=int(input("enter rate: "))
simple_interst=(price*time*rate)/100
print(simple_interst)

#celsius to fahrenheit formula
celsius=float(input("enter celsius value: "))
F=(celsius*9/5)+32
print(f"the converted value of{celsius} fahrenheit is {F}")

# find average number
a=int(input("enter a number: "))
b=int(input("enter b number: "))
c=int(input("enter c number: "))
average_number=(a+b+c)/3
print(f"average number is {average_number}")

#calculate area of circle
radius=float(input("enter the area of circle: "))
area=3.14*radius*radius
print("area of the circle",area)