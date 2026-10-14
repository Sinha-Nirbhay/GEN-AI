print("____________________ Approach - 1 _______________________")

#decorator Function
def my_decorator(func):
    def wrapper(*args , **kwargs):
        print("Before Function")
        func()
        print("After Function")
    return wrapper

#original say_hello function
def say_hello():
    print("Hello!")

# decorated say hello function
decorated_say_hello = my_decorator(say_hello)
decorated_say_hello()
 
 
print("____________________ Approach - 2 _______________________")

#decorator Function 
def my_decorator(func):
    def wrapper(*args , **kwargs):
        print("Before Function")
        func()
        print("After Function")
    return wrapper

"""Original say_hello function change to decorated say_hello function. 
One more way to decorate function but in this approach original function modified directly"""
@my_decorator
def say_hello():
    print("Hello!")
 
say_hello()


print("____________________ Approach - 3 _______________________")


# decorator function
def add_greeeting_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + " Have a great day! "
    return wrapper

# Original parameterized function
def say_hello(name):
    return f"Hello + {name}!"

# Decorated parameterized function
custom_say_hello = add_greeeting_decorator(say_hello)
print(custom_say_hello("Nirbhay"))

print("____________________ Approach - 4 _______________________")


# decorator function
def add_greeeting_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + " Have a great day! "
    return wrapper

# Original parameterized function
@add_greeeting_decorator
def say_hello(name):
    return f"Hello + {name}!"

print(say_hello("Nirbhay"))