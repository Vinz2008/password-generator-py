#!/usr/bin/python

import random
passlength = input("How much character do you want in your password ?")
passlength = int(passlength)
answerCharsNb = input("Do you want numbers in your password ? (y/n)")
if answerCharsNb == "y" :
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*()?"

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*()?"
passlength
password =  "".join(random.sample(chars,passlength ))
print (password)
