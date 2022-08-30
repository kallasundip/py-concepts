# Write a program to find the largest number in a list
numbers = [2, 444, 5, 88, 4, 5, 8, 85]
max = numbers[0]
large_num = 0
for number in numbers:
    if number > max:
        max = number
print(max)


#2D List
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0][1])

for row in matrix:
    print(row)
    for item in row:
        print(item)

value = [2,2,5,5,1,1,8,44,44]
number2 = []
for item in value:
    if item not in number2:
        number2.append(item)
print(number2)