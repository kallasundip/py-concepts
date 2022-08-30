'''
import random as rd
rand_value = rd.randint(11,99)
number = 59
# rev_num = 0
# remainder = number % 10
# rev_num = (rev_num * 10) +remainder
# number = number //10
# print(format(rev_num))
revs_number =0
while (number > 0):
    # Logic
    remainder = number % 10
    revs_number = (revs_number * 10) + remainder
    number = number // 10
print("The reverse number is : {}".format(revs_number))

'''

# the number to be reversed
num = 97402

#convert number to string
num_string = str(num)

# store the size of the number
size = len(num_string)

# use slicing to reverse
reversed_num = num_string[size::-1]

#output reversed number
print("Reversed Number is: " + reversed_num)
