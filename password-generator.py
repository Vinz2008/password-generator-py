#!/usr/bin/python

import random
passlength = input("How much character do you want in your password ?")
passlength = int(passlength)
answerCharsNb = input("Do you want numbers in your password ? (y/n)")
answerCharsSpecial = input("Do you want special characters in your password ? (y/n)")
if answerCharsNb == "y":
    if answerCharsSpecial =="y":

    if answerCharSpecial == "n":    
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*()?"
if answerCharsNb == "n":
    
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*()?"

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*()?"

password =  "".join(random.sample(chars,passlength ))
print (password)
