# task: genrate a random_password
# input: length
# output: random_password

import random
import string
password_length=int(input('enter length password\n'))


if password_length<3:
    print("sorry the password is week 😔")
else:
    number_upper = number_lower = number_digits = password_length // 3
    number_digits += password_length % 3

    upper_list = random.choices(string.ascii_uppercase , k=number_upper)
    lower_list = random.choices(string.ascii_lowercase, k=number_lower)
    digit_list = random.choices(string.digits, k=number_digits)

    password_list = upper_list + lower_list + digit_list

    random.shuffle(password_list)
    
    password = "".join(password_list)
    print("here is your password:", password)
