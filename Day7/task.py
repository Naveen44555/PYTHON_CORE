print("even") if True else Print("odd")  #terinary operator
#                          Task
x=10   # here we assign a value to variable
def show(): #function and we give on function name
    x=5    #second variable with value
    print(x)   #here print method we use to print
show()          #function calling
print(x)        # print the output
#output: 5
#        10

def outer():  # function & name
    x=10        #variable and value
    def inner():    #second function with name
        print(x)        #print the output
    inner()
outer()
#output: 10

x="global"      #here global it means global is applicable for all inside the program
def outer():        #funtion with name
    x="outer"       #variable and value
    def inner():    #second function
        x="inner"   #second variable with value
    inner()         #function calling
    print("outer:",x)   #print output
outer()                  #function calling
print("global:",x)       #print output
#output :outer: outer
#        global: global