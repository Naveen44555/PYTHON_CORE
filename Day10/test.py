a=["naveen"]
b=[1,2,3]
c=[11.2,44.4]
print(type(a),type(b),type(c),)

t=[[1,2],3]
t[0].append(4)
print(t)

s=''
for i in range (4):
    if i%2==0:
        s+='A'
    else:
        s+='b'
print(s)

word="python"  #slicing
print(word[1:4]+word[-1]+word[ :1])

result=(3+4)*2**2-5
print(result)

print((3+4)*2**2-5)

list1=[1,2,3,4,5,6,7,8,9,10]
count1=0
count2=0
for num in list1:
    if num%2==0:
        count1+=1
    else:
        count2+=1
print("number of even numbers are:",count1)
print('number of odd numbers are:',count2)

list1=[23,43,28,57,12,11]
max

list1=[23,43,28,57,12,11]
largest=list1[0]
for num in list1:
    if num>largest:
      largest=num
print(largest)

str1="TENET"
palindrome=True


str1="racecar"
rev=str1[::-1]
if str1==rev:
    print("palindrome")
else:
    print("not palindrome")

str1='abc123xyz456'
sum=0
for i in str1:
    if i in '0123456789':
      sum+=int(i)
print(sum)

list1=[1,2,2,3,1]
empty=[]
for i in list1:
    if i not in empty:
        empty.append(i)
print(empty)