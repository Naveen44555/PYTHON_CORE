# # #prime number or not
# num=int(input("number:"))
# if(num>1):
#     for i in range(2,num):
#         if num%i==0:
#             print("not prime")
#             break
#     else:
#        print("prime")
# else:
#     print("invalid number")

# num=int(input("enter number :"))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print(num,"is not prime number")
#             break
#     else:
#         print(num,"is prime number")
# else:
#     print("not prime number")


# num=int(input("enter a number: "))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print(num,"not prime number")
#             break
#     else:
#             print(f"{num} is prime number")
# else:
#     print(num,"it is not prime number")

# # num=int(input("enter a number:"))
# # if num>1:
# #     i=2
# #     while i<num:
# #         if num%i==0:
# #             print(num,"not a prime number ")
# #             break
# #         i+=1
# #     else:
# #         print(num,"it is prime number")
# # else:
# #     print(num," is not prime number")
   
# # num=int(input('enter number:'))
# # if num>1:
# #      for i in range(2,num):
# #          if num%2==0:
# #              print("not prime number")
# #              break
# #      else:
# #          print("it is prime number")
# # else:
# #     print("not prime")

# num=int(input("enter"))
# if num>1:
#     i=2
#     while i<num:
#         if num%2==0:
#             print("not prime")
#             break
#         i=i+1
#     else:
#         print("it is prime")
# else:
#     print("not prime")


# num=int(input("enter number :"))
# if num>1:
#     for i in range(2,num):
#         if num%i==0:
#             print(num,"is not prime number")
#             break
#         else:
#             print(num,"is prime number")
# else:
#     print("not prime number")

num=int(input("number"))
# count=0
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(num,"not prime")
            break 
    else:
        print("prime")
else:
    print("not prime")
        