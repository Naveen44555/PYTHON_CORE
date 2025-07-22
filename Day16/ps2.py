# num=int(input("enter number:"))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print("not prime number")
#             break
#     else:
#         print("prime number")
# else:
#     print("not prime number")


# # user=input("enter number:")
# a=5
# b=2
# c=44
# if a>b and a>c:
#     print("a is bigger")
# elif b>c:
#     print("b is bigger")
# else:
#     print("c is bigger")


# #second largest
# a=88
# b=8
# c=8
# if (a>b and a<c) or (a<b and a>c):
#     print("a is second largest")
# elif (b>a and b<c) or (b<a and b>c):
#     print("b is second largest")
# else:
#     print("c is second largest")
    
   
# num1=int(input("enter number:"))
# num2=int(input("enter number:"))
# choice=int(input("ente number 1 or2 or 3 or 4 for operation :")) 
# for choice in range(1,5):
#     if choice==1:
#      result=num1 + num2
#      print(result,"addition process")
#     elif choice==2:
#       result=num1 - num2
#       print(result,"sub ")
#     elif choice==3:
#         result=num1 * num2
#         print(result,"multiplication")
#     elif choice==4:
#          result=num1/num2
#          print(result,"division")
# else:
#     print("you enter wrong number")


num1=int(input("enter number:"))
num2=int(input("enter number:"))
choice=int(input("ente number 1 for addition,2 for subtraction 3 for multiply 4 for division :")) 
if choice==1:
     result=num1 + num2
     print(f"here we done addition after {result}")
elif choice==2:
      result=num1 - num2
      print(f"here we done subtracation after {result}")
elif choice==3:
    result=num1 * num2
    print(f"here we done multiply after {result}")
elif choice==4:
    result=num1/num2
    print(f"here we done division after {result}")
else:
     print("you enter wrong number so please check ")


string="naveen"
