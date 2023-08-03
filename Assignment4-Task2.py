# list of non-repeating random numbers

import random

print("Enter your range of numbers and number of non-repeating random numbers that you want and recieve them in a list below.")

start = int(input("Enter the starting number of the range:"))
end = int(input("Enter the ending number of the range:"))

count = int(input("Enter the number of non-repeating random numbers you want in your list:"))

if count > (end - start+1):
    print("Error! your number cannot be greater than your range size.")

nums = random.sample((range(start, end+1)),count)

print("Here is your list:",nums)