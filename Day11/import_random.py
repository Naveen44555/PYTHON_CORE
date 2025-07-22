import random  #it returns value between 0.0 to 1.0
# print(random.random())
print(random.random(2,3))

#uniform (range between 10 to 20)
print(random.uniform(10,20)) # here returns b/w 10  to 20 value

# #randint  (range between 10 to 20)
# print(random.randint(10,20)) # here returns b/w 10  to 20 value

#choice  # randomly take
a=[1,3,5,4,64,65,33,34]
# print(random.choice(a))  #only one number

# #choices
# print(random.choices(a,k=6))  #list lo vasthundi & same value can give (repeated)
 
# #sample         -              diff values (unique)
# print(random.sample(a,k=6))

#shuffle 
random.shuffle(a)   # 
print(a)