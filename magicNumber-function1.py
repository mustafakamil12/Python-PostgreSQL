#!/usr/local/bin/python3
import random

def ask_user_and_check_number():
	user_number = int(input("Enter a number between 0 and 9: "))
	if user_number in magic_number:
		print("You got the number right!")
	if user_number not in magic_number:
		print("You didn't quite get it!.")

#magic_number = [3,9]
magic_number = [random.randint(0,9),random.randint(0,9)]
chance = 3
for attempt in range(chance):	# range(chance) is [0,1,2]
	print("This is attempt {}".format(attempt+1))
	ask_user_and_check_number()

