#palindrome
number=12321
rev=0
permanent=number
while number>0:
    td=number%10
    rev=rev*10+td
    number=number//10
if rev==permanent:
    print("it is palindrome")
else:
    print("it is not palindrome")

# for x in "banana":
#     print(x)

# fruits={"apple","banana","grapes"}
# for x in fruits:
#     print(x)
#     if x=="banana":
#        break

# # Break
# fruits={"apple","banana","grapes"}
# for x in fruits:
#     if x=="banana":
#        break
#     print(x)

# fruits={"apple","banana","grapes"}
# for x in fruits:
#     if x=="banana":
#        continue
#     print(x)

# #range
# for i in range(6):
#     print(i)

# for i in range(1,8):
#     print(i)
#     if i==6:
#         break
# else:
#     print("finished")

# for i in range(1,8):
#     print(i)
#     if i==6:break
# else:
#     print("finished")

# # nested for
# list="naveen","shanni","nagaraj"
# for i in list:
#     for x in i:
#       print(i)

# list="naveen","shanni","nagaraj"
# fruits="banana","grapes","apple"
# for i in list:
#     for x in fruits:
#         print(i,x)

# for i in [0,1,2]:
#     pass
