# guess numbers

import random

print("Play with me! Guess a number between 0 and 20 and see if it's what I picked!")

pc_number = random.randint(0,20)
i = 0
while i < 5:
    user_number = int(input("Enter your guess:"))
    i += 1
    if user_number == pc_number:
        print("You won!")
        break

    if user_number < pc_number:
        print("Go up")

    if user_number > pc_number:
        print("Go down")

print("Your guess count:",i)