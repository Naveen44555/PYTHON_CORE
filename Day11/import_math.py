import math
#  ceil
print(math.ceil(2.9))
print(math.ceil(4.1))
print(math.ceil(2.0))

#floor
print(math.floor(4.9))
print(math.floor(4.1))

#truncate  - removes decimal values
print(math.trunc(111.4))
print(math.trunc(166.87788))
print(math.trunc(199.9))

#factorial
fact=1
for i in range(1,6):
  fact*=i
print(fact)

#constant functions
# mathematical functions
print(math.pi)   #pi value
print(math.e)  # logarithms
print(math.inf)  #infinity
print(math.nan)   #nan value in excel

# # exp()  
# print(math.exp(10)) # without math module funtions
# print(pow(math.e,10)) # with math module funtions

# # logarithms 
# # log()
# print(math.log(8,2))
# print(math.sqrt(25))

#trignometric functions
a=math.degrees(90)
b=math.pi
print(round(math.sin(b/2)))
print(round(math.cos(b/2)))
print()