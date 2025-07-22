# n=11,12
# for i in n:
#     print(i)

# n=11
# for i in range(1,n+1):
#     print(i)

# given_range=10
# for i in range(given_range):
#     if i%2==0:
#         print(i)

# given_number=10
# temp=0
# for i in range(given_number):
#     temp=temp+i
# print(temp)

# number=1,2,3,4
# temp=0
# for i in number:
#     temp=temp+i
# print(temp)

# #sum
# num=1,2,3,4
# temp=0
# for i in num:
#     temp=temp+i
# print(temp)

# #range sum
# g_number=10
# sum=0
# for i in range(1,g_number+1):
#     sum=sum+i
# print(sum)

# num2=12345
# temp=0
# while num2>0:
#     td=num2%10
#     temp=temp+td
#     num2=num2//10
# print(temp)

#reverse

num2=1234321
temp=0
pa=num2
while num2>0:
    td=num2%10
    temp=temp*10+td
    num2=num2//10
if pa==temp:
    print("palindrome")
else:
    print("not palindrome")

num=1,2,3,4
temp=0
for i in range(num):
    temp=temp+i
print(temp)




