


# # sum of all digits in given num
# num=125
# sum=0
# while(num>0):
#     Ld=num%10
#     sum+=Ld
#     num=num//10
# print(sum)

# # sum of squares of all digits in given num
# num=125
# sum=0
# while(num>0):
#     ld=num%10
#     sum+=ld**2
#     num=num//10
# print(sum)

# # to find the count of total digits in given num using while loop
# num=12504
# count=0
# while num>0:
#     ld=num%10
#     count+=1
#     num=num//10
# print(count)

## reverse a num 





# #rev=5
# revx10+1d==>5X10+2=52

# reverse a number
# num=123654
# rev=0
# while(num>0):
#     ld=num%10
#     rev=rev*10+ld
#     num=num//10
# print(rev)

# given number is palindrome or not
num=123654
num1=num
rev=0
while(num>0):
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)
if(num==rev):
    print("given num is palindrome")
else:
    print("given num is not palindrome")
    
# num=123654
# num1=num
# rev=0
# if(num%10!=0):
#     rev=0
#      while(num>0):
#       ld=num%10
#       rev=rev*10+ld
#       num=num//10
#    print(rev)
#    if(num==rev):
#      print("given num is palindrome")
#    else:
#      print("given num is not palindrome")
# else:
#     print("give numbers which are non divisible by 10 becase we cannot check for palindrome")
    
#armstrong numbers
# 125 is armstrong number

