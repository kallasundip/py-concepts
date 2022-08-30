'''
    --- Exit code 0 means the code excetued sucussfully
    --- insted of 0, we gat 1 or any number means the program crashed because invalid value
    --- by using exception we can print proper error message
    --- try and except
'''
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age

    print(age)
    print(risk)

except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Age can not be 0")


