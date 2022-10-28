#use diceware
#input number of words in passphrase (first for loop)
#integrate the dice roll to get the numbers for the words (second loop)
#do all of the above and put all the numbers in a list (maybe) and at the end translate those numbers into the words and return them

import random

dice_numbers = '123456'
dice_roll = ''
num_words = int(input('How many words in the passphrase?:'))


for i in range(5*num_words):
    dice_roll.append(random.randint(dice_numbers))

