user_input = "1,2,3,4,5,6"
user_numbers = user_input.split(",")

user_numbers_as_int = [int(number) for number in user_numbers]

print(user_numbers_as_int)