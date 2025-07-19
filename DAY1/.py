#First program in python

print("hi naveen")

print('hey"good morning"')

print("hello\npython world\nhelloworld")

print("hey"+" print('naveen')")

b=10+5
print(b)

c="naveen"
print("hi"+" "+ input('what is your name : ')+"  " +"you are looking good")

print("your weight is:"+ input('enter your weight is:'))

print(f"hi {c} you are looking good.")

print ("hi Parthanaboina")

print("good evening")

print('print("what to print")')
print("hello","honey")

print("hello" "nn")
print("hello"+" "+"naveen")

print("string manipulation exercise")
print('string manipulation is done with "+"sign')

print('e.g.print("Hello"+"jenny")')
print("New lines can be created with a backslash and n")
print("hello world \nhello world\nhello world")

# input("what is your name?")
print("hey"+" "+ input('what is your name:')+"  how are you")

# comments in python
print('1.single line comment - #') # single line
# start with(#) ,only one line comment we can use ,compiler and interpreter are ignores                            
 
print("2.multi line comment - ''' ''' ")   
'''in coding multi lines of comments this we can use 
save treees 
save water
Be happy
'''             

student=input("enter student name:")
course=input("enter course name:")
city=input("enter city name:")
#jeswanth joined python course in hyd
print(f"{student} joined {course} course in {city}")           

#variables - its like container
a=22 
print(a) 

_nn="honey" 
print(_nn)
print(id(_nn))

a12=100
print(a12)

name=input("what is your nick name: ")
length=len(name)
length1=f"length of your name is len{length}"
print(length1)

a=input('enter value of a=')
b=input('enter value of b=')
temp=a
a=b
b=temp
print('a value ='+a)
print('b value =',b)

x=555
y=555
print(id(x)) #it allocates same memory location
print(id (y))#

x=33
y=33
print(id(x)) #it allocates same memory location
print(id (y))# same memory allocates 
 
# memory pooling

x=5             # short range is (-5 to 256)
y=58
print(id(x))        # we get same address for both because its short range and positive value
print(id(y))        

print('naveen')

x=-557    #short range is (-5 to 256)
y=-557
print(id(x))   # we get same address for both x & y 
print(id(y))

# interning

a="hello"
b="hello"
print(id(a))  
print(id(b))        # we get same address for both because its short range and positive value