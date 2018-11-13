#password generator

#import libraries
import random
from random import randint

#specify the letters/numbers/characters for the computer to use
lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
letters = lower + upper
numbers = "1234567890"
chars = "!@#$%&*-_?"

#generate a random number for the length of the password to be
randomNumber  = int(random.randint(4,15))

#code to be run
for i in range(randomNumber):
    if randomNumber >= 6:
        password = random.choice(letters + numbers)
        print(password ,  end = "")
    else:
        password = random.choice(letters + numbers + chars) #chooses random letter, number, or character
        print(password, end = "")                           #print the password
