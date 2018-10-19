#password generator

#import libraries
import random
from random import randint

#specify the letters/numbers/characters for the computer to use
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = lower + upper
numbers = "1234567890"
chars = "`~!@#$%^&*()-_+=|[]\/?'"

#generate a random number for the length of the password to be
randomNumber  = int(random.randint(6,15))

#code to be run
for i in range(randomNumber):
    password = random.choice(letters + numbers + chars) #chooses random letter, number, or character
    print(password, end = "")                           #print the password
