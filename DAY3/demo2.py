'''
int
float 
complex
bool
boolean'''
'list,tuple,dictionary,set'

'''int a=1
float b=5.5 (decimal point)
complex c=2+3j (2 is real part)
             (3j is imaginary part)
             '''
#bool= true or false
#strings = (' " ''')

a=4
print(type(a))

b=8.8
print(type(b))

c=8+9j
print(type(c))

a='naveen'
print(type(a))

a=22
print(float(a))

b=8.9
print(int(b))

#case sensititive
naveen=2
NAVEEN=22
print(NAVEEN)

a=True
b=False
print (type(a),type(b))

print(True==1)
print(False==0)

#types lo convert chesinappudu manaku data loss avuthundi daniki idi
#if data loss- explicit type conversion
#no data loss - implicit type conversion

f=3+4j #complex
print((f),type(f))

g="ground" #str
print(type(g))

var=True  #bool
v=6>3
print(type(v)) 

h=23 #type conversion
j=55.6
print(float(h))
print(int(j))
print("naveen")

value_1=33
print(id(value_1))
value_1=43
print(id(value_1))

print(value_1)

char_a='A'#ascii values
ascii_a=ord(char_a)
print(ascii_a)

c='b'
a=ord(c)
print(a)

char_b='B'
ascii_b=ord(char_b)
print(ascii_b)

a=65
ascii_a=chr(a)
print(ascii_a)


var_1=0o22
var_2=0x12
print(var_1)



var_name1=input("enter first number:" )
var_name2=input("enter second number:")
sum=var_name1+var_name2
print(sum)

number=input("enter two digit number:")
first_digit = number[0]
second_digit =number[1]

print(int(first_digit) + int(second_digit ))

# List

fruits=["apple","mango","banana"] # collection of strings and list of fruits
print(id(fruits))

fruits[1]="pineapple"

print(id(fruits))


ids=[1,2,3,4] #collection of integers and list of ids
prices=[125.67,256.2,450.2,116.22] #collection of floatingvalues and list of prices
mixed=[1,2,"hi",12.5,True]
print(type(fruits))
print(type(ids))
print(type(prices))
print(type(mixed))

#so we can say a list can be a collection of homogeneous / heterogeneous elements.

a="harish"
print(id(a))
a="kiran"
print(id(a))


x=[1,2,3]
print(len(x))

print(x)

x=[]+[4]
print(x)

list=[1,2,"hi","hello","somthing",[1,2,3],5,67]

op=list+["python"]+[12]

print(op)


str="hello  world"
str1="welcome"

print(str[-1])


fruits=["apple","mango","banana"]
print(fruits[0],fruits[2])
print(f"total number of fruits are {len(fruits)}")
fruits[1]="pinapple"
print(fruits)

x=["harish","naresh","suresh","mahesh"]
print(id(x))
x[2]="kiran"
print(x)

data=[1,2,[4,5],[6,7],8,["something"]]
print(data[2][0])
print(data[3][1])
print(data[5][0][2])

mixed=[1,2,"hi",12.5,True]
print(f"value:{mixed[0]},Type:{type(mixed[0])}")
print(f"value:{mixed[2]},Type:{type(mixed[2])}")

# tuples

days=("sun",["mon"],"tue",(1,2,3)) #defining a tuple

print(f"size of the tuple is {len(days[3])}") #size of the tuple is 3

days[1]="fri" #-->accessing elements from tuple

print(type(days))
#checking type

print(len(days)) #to find the size of the tuple

print(days[1][0]) #accessing nested elements in tuple


#set

sets={1,2,34,5,5,2,1} #normal set
print(type(sets))
print(sets)

sets.add("hi") # add() method is used to add the element into the set
print(sets)
sets.remove(2) #remove() method is used to remove the element from the set
print(sets)

# frozenset

# it is also a collection of unordered elements , but here we can't add/remove elements into the set

sets1=frozenset([1,3,5,7,8,8]) #here iam defining a frozenset

# sets1.add(4) # trying to add value 4 into the frozenset

# sets1.remove(5) #trying to remove the value 5 from the frozenset

print(type(sets1))


#dictionary

realme_info={"name":"realme",
             "model":"5c",
             "price":25000,
             "ram":"8gb",
             "colors_available":["black","green","red","white"],
             "camera":"50mp"
             }

My_info={"Name":"Naveen",
         "age":23,
         "gender":"male",
         "height":5.4,
         "address":{"d.no":2-85/1,
                    "street":"gramapanchayat road",
                    "landmark":"temple beside",
                    "mandal":"nereducherla",
                    "dlstrict":"suryapet",
                    "state":"Telangana",
                    "pincode":508218,
                    },
         "is_he_married":"False",
         "skills":["Html","css","javascropt","python"]
         }


My_info["height"]=5.6 #updating keys in dictionary

My_info["fav_food"]="biryani" #adding new property into the dictionary

# to store the properties of a particular thing
#collection of key-value pairs
#collection of multiple properties