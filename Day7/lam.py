#topics:
# lambda function
# terinary operator

'''lambda function :
1.we don't need def key word
2.we don' need lambda keyword
3.we don't need function name 
4.we don't use paranthesis or open brckets()
5.with out using return keyword
'''
nnn= lambda :"hello world" #here we give variable and assign lambda function
print(nnn())
n=lambda :"naveen"
print(nnn())

pn=lambda :"PARTHANABOINA NAVEEN"
print(pn())

integer_values = lambda :"2,4"
print(integer_values())


op=lambda x:x+5  # addition operator
print(op(9))

naveen=lambda n:n-6 #subtraction operator
print(naveen(9))

ss=lambda r:r*4  #multiplication operator
print(ss(6))

#scope: local scope, global scope, enclosed scope

x=10
def func1():
    print(x)
func1()

def sample(): #name error we didm't give print(x)
    x=5
    print("hello")
sample()
print(x)


def func1():
    print(x)
    def func2():
        x=10
    func2()
func1()  


