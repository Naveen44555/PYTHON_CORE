#statements-----> 1. normal statemnt
 #                2. control statement
 #control statements---->1.conditional and Looping
'''conditional statement are used for decision making purpose.
1.simple if 
2.if-else
3.nested if 
4.nested elif
5.terinary operator'''

#simple_if
condition=True
if (True):
    print("you win")
print("this is if statemnt")

#if_else
No_water_in_tank =True
if(False):
    print("yes there is no water in tank")
else:
    print("water is fully in tank")
    
#enter your age while you are eligible for vote
age=int(input("enter your age: "))
if age>=18:
    print (f"your age is {age} you are eligible to vote")
else:
    print (f"your age is {age} you are minor not eligible for vote")

number=int(input("enter a number to check it is even or odd:"))
if(number%2==0):
    print("it is even number")
else :
    print(f"you enterd {number} it is odd number")
print("bye....")

# nested_if

if True:
    print('nenu naveen')
    if True: 
       print ("nenu kuda naveen") 
    else:
        print("iam naveen")
else:
    print("jj")
        
# nested if
if True:
    print("you are naveen")
    if False:
        print("you naveen")
else:
     print("naveen")   
        
#elif        
if True:
  print ("iam if")
elif True:
    print("iam elif")
elif False:
    print("nenu elif naveen")
else:
    print ("iam else")       
      
num=123335
if(num & 1==0):
    print("even")
else:
    print("odd")
    
num=1
if(num & 1==0):
    print("even")
else:
    print("even")
    
#convert
seq="02468"
ip=125701
cnvrt=str(ip)
if(cnvrt[-1] in seq):
  print("even")
else:
    print("odd")
    
seq=[0,2,4,6,8]
ip=1123
cnvrt=str(ip)
if(int(cnvrt[-1])in seq):
    print("even")
else:
    print("odd")
 
m=20
p=37
c=50
if(m>=35 and p>=35 or c>=35):
    print("you are promoted")
else:
    print("you failed")
 
amount=5725
notes_1000=amount//1000 
rem_change=amount-(notes_1000*1000)  #amount%1000
notes_500=rem_change//500
rem_change=rem_change-(notes_500*500)  #rem_change%500
print(notes_1000,notes_500,rem_change)
    
    
persons=int(input("enter how many members "))
if(persons<=5):
    print("we want 1 car")
elif(persons<=10):
    print("2 cars")
elif(persons<=15):
   print("3 cars")
else :
    print("each 5 members want 1 car")
# elif(persons%==5):
#     print(f"persons are{persons} we want")
    
    
number=625
res=number**0.5
print(res)
print(res==int(res))
print(res)