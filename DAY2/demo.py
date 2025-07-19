#variables - its like container
a=22 
print(a) 

_nn="honey" 
print(_nn)
print(id(_nn))

a12=100

name=input("what is your nick name: ")
length=len(name)
print(length)

a=input('enter value of a=')
b=input('enter value of b=')
temp=a
a=b
b=temp
print('a='+a)
print('b=',b)

x=33
y=33
print(id(x)) #it allocates same memory location
print(id (y))# same memory allocates 
 
# memory pooling

x=5             # short range is (-5 to 256)
y=5
print(id(x))        # we get same address for both because its short range and positive value
print(id(y))        


x=-557    #short range is (-5 to 256)
y=-557
print(id(x))   # we get different address for both x & y 
print(id(y))

# interning

a="hello"
b="hello"
print(id(a))  
print(id(b))        # we get same address for both because its short range and positive value







