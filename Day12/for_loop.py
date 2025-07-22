#break
for i in range(1,10):
    print(i)
    if i==5:
        break

for x in range(1,10):
    if x==5:
        break
    print(x)

for x in range(1,10):
    print(x)
    if x==6:
        print("here 6")
        
# continue
for x in range(1,10): #here we give print firstly
    print(x)
    if x==6:
        continue

for i in range(1,10):
    if i==6:
        continue
    print(i)

stops=["kphb","srnagar","ameerpet","paredground","paradise","sec"]
for i in stops:
    if i=="ameerpet":
        continue
    print(i)    #end=" "

# print even numbers from 1 to 10
for i in range(1,21):
    if i%2==0:
     print(i)
    else:
        print(i,"odd")

a=(1,20)
for i in a:
    if i%2==0:
        print(i,"even")
    else:
        print(i,"odd")

for i in range(2,11,2):
    print(i,"even number")

for i in range(1,11,2):
    print(i)
        
'''Loop Starts: The for loop goes through each item in the list one by one.
First: x = "kphb"
Then: x = "srnagar"
Then: x = "ameerpet"
Condition Check:
When x == "ameerpet", the condition becomes True.
Break:
The break stops the loop immediately. So the loop ends at "ameerpet".
Print:
After the loop, print(x) runs.
Since x is "ameerpet" at the time of break, it prints:'''

# see diffference
stops=["kphb","srnagar","ameerpet","paredground","paradise","sec"]
for x in stops :
   if x=="ameerpet":     
       break 
print(x)   
   
stops=["kphb","srnagar","ameerpet","paredground","paradise","sec"]
for x in stops :
   if x=="ameerpet":     
       break 
   print(x) 

stops=["kphb","srnagar","ameerpet","paredground","paradise","sec"]
for x in stops :
   print(x) 
   if x=="ameerpet":     
       break
   print(x)

# while loop
list=("banana","apple","cherry")
x=0
while (x<len(list)):
    print(list[x])
    x+=1

y=1
while(y<=10):
    print(y)
    y+=1

flashsale=True
while(flashsale):
    print("ddd")

# print even numbers from 1 to 10 in while
num=2   # even numbers
while num<=20:
    if num%2==0:
        print(num)
    num+=1

num=1
while (num<=30):
    if num%2!=0:
        print(num)
    num+=1

naveen=1
while(naveen<=30):
    if naveen%2!=0:
        print(naveen)
    naveen+=1

naveen=2
while(naveen<=30):
    if naveen%2==0:
        print(naveen)
    naveen+=1
print(naveen)

num=2  
while num%2==0 and num<=20:
    print(num)
    num+=1

num=1
while (num<=20):
    print(num)
    num+=1

num=1
while num<=20:
    if num%2==0:
        print(num)
    num+=1

naveen=1
while(naveen<=30):
    if naveen%2!=0:
        print(naveen)
    naveen+=1

naveen=2
while(naveen<=30):
    if naveen%2==0:
        print(naveen)
    naveen+=1
print(naveen)

    
# reverse print
x="ollom"
op=""
for chr in range(len(x)-1,-1,-1):
    op+=x[chr]
print(op)


if (op==x):
    print("it is palindrome")
else:
    print("it is not palindrome")

str="hello"
op=""
for i in range(len(str)-1,-1,-1):
    op+=str[i]
print(op)


naveen="yadav"
op=""
for x in range(len(naveen)-1,-1,-1):
    op+=naveen[x]
print(op)

str="2345"
op=""
for i in range(len(str)-1,-1,-1):
    op+=str[i]
print(op)

x=input("enter a string")
str=""
y=len(x)-1
while y>=0:
    str+=x[y]
    y=1