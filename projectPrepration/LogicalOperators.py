x = 99
y = 999
z = 9999

if x == 9:
    print("X value is :", x)
elif x==99:
    print("Y vlue : ", y+1)

else:
    print("y Value: ", y)


#   Logical Operators
if x==9 and y==999:
    print(z)

if x==9 or y==999:
    print(z)

if x == 99 and not y==99:
    print("------", x)


house_prise = 1000000

if house_prise == 1000000:
    down_payment = 0.1 * house_prise
else:
    down_payment = 0.2 * house_prise
print(f"Down Payment Rs.{down_payment}")
