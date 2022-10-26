#how to improve this and develop it further (maybe even to its own app/program)
#make it create a file that registers all the passwords that have been used and their respective email address and website
#make it a secure (maybe encrypted) file
#password manager

import random

characters = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789,.-;:_~^´`+*?«»<>!#$%&/()=}][{£@"\|'

number_characters = int(input('How many characters would you like your new password to have?:'))
password = ''

for n in range(number_characters):
    password += random.choice(characters)

print(password)