import random

characters = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ0123456789,.-;:_~^´`+*?«»<>!#$%&/()=}][{£@"\|'

number_characters = int(input('How many characters would you like your new password to have?:'))
password = ''

for n in range(number_characters):
    password += random.choice(characters)

print(password)