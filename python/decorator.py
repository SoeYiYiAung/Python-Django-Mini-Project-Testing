# Decorator -> define work before and after main function
def greet(fun):
    
    def wrapper(name):
        print("hello") #before our function
        fun(name)
        print("good bye") #after our function
    return wrapper

@greet
def SayName(name):
    print(name)
SayName('soe yiyi')