'''
    ---- Logical Operators in Python
1. and
2. or
3. not
'''

x = 99
y = 999
z = 9999
a = 99
if x==9 and y==999:
    print(z)

if x==9 or y==999:
    print(z)

if x == 99 and not y==99:
    print("------", x)

'''
    ---- Conparisoon Operators
<, >, <=, >=, ==, !=
'''
if x > y:
    print("X is Greater than y: ", x)
else:
    print("y is Greater than x: ", y)

if x<y:
    value = y
else:
    value = x
print(f"Y value is {value} Greater than x value {x}: ")

if a<=x:
    print(f"a value is {a}")

if y>=x:
    print(f"y value is {y}")

if x != y:
    print(f"x and y values are not equal {x} and {y}")

# Weight Converter
weight = int(input("Weight: "))
weight_type = input("(P)pounds or (K)g: ")
if weight_type.upper() == "P":
    print("Weight in pounds: ", weight * 0.45)
else:
    print("weight in kg: ", weight / 0.45)