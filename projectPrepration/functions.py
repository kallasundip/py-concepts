'''
    --- Functions
    --- It is a better way to organise the code
    --- we need to break up the code into smaller, more manageable, more maintainable call called functions
    --- A Functions is a container for a few lines of code at perform a specific task
    --- For creating of function we use reserved key work in python def
'''
'''
    --- by default all functions in the python return none
    --- we cah change that the function calculate some thing we can return the result 
        using return statement 
'''


def greet_user(name):
    print("Hi ", name)
    print("This is my First function")


def greet_userr(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")


print("Start")
greet_user("raju")
greet_userr("raj", "kumar")
greet_userr(last_name="kumar", first_name="Raju")
print("Finish")


def square(number):
    return number * number


print(square(3))




