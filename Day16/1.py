
#1. print even numbersin the range of 1to 20

# for i in range(1,21):
#     if(i%2)==0:
#        print(i)      # print(i, end=" ")
#     elif (i%2!=0):
#         print()
        
# #2.print odd numbers
# for i in range(1,101):
#     if i%2!=0:
#         print(i,end=" ")

# #3.print numbers which are divisible by 5 from 1 to 50
# for i in range (1,51):
#     if i%5==0:
#      print(i,"ii")
#     else:
#         print("kk")

# print"it is divisible by 5" if 

# #4.print multiples of 3, multiples of 5, and multiples of 3 and 5 from 1 to 50
# for i in range (1,51):
#     if i%3==0 and i%5==0:
#         print(i,"it is divisible by 3 and 5")
#     elif i%5==0:
#         print(i,"divi by 5")
#     elif i%3==0:
#         print(i,"divisible by 3")
#     else:
#         print(i)

#5. find the number of numbers divisible by both 3 and 7 from 1 to 100

# count=0
# for i in range


# if today is sunday then what day after 365 days ? 
days=['m','t','w','th','f','sat','s']
today_index=6
future_index=(today_index + 393) % 7
print(days[future_index])

days=['m','t','w', 'th', 'f','st', 'sd']
today_index=6
future_index=(6+499)%7
print(days[future_index])