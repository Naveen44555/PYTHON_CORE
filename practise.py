# print(str(10))

# print(bool(""))
# print(bool('hello'))

# x=[1,2,3]
# y=[1,2,3]
# print(x is y)
# print(x==y)
# print(id(x))  #diff
# print(id(y))  #diff

# x=(1,2,3)   #true
# y=(1,2,3)
# print(x is y)

# x={1,2,3}   #false
# y={1,2,3}
# print(x is y)

# x=[1,2,3]   #true
# y=x
# print(x is y)

# a=9 # same
# b=9
# print(id(a),id(b))

# # print('n')

# a=9 # same
# b=a
# print(id(a),id(b))

# x=[1,2,3]
# y=x.copy()
# y.append(4)
# print(x)

x=[1,2,3]
y=x
y+=[4]
print(x)