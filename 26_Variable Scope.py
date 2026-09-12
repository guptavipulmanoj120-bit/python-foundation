#The two main types of variable scope 
#1) local variable scope → variables defined inside a function are local to that function and cannot be accessed outside of it
#2) global variable scope → variables defined outside of a function are global and can be accessed inside functions

# local variable

def student():
    name = "Vipul"   # Local variable
    print(name)

student()

# global varibale 

message = "Hello"

def greet():
    global message
    message = "Hi"

greet()

print(message)

