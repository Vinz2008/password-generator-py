#!/usr/bin/python

import random
passlength = input("How much character do you want in your password ?")
passlength = int(passlength)
answerCharsNb = input("Do you want numbers in your password ? (y/n)")
answerCharsSpecial = input("Do you want special characters in your password ? (y/n)")
answerCharsCapital = input("Do you want Capital letters in your password ? (y/n)")
if answerCharsNb == "y":
    if answerCharsSpecial =="y":
        if answerCharsCapital == " y":
        if answerCharsCapital == "n":

    if answerCharSpecial == "n":    

if answerCharsNb == "n":
    if answerCharsSpecial =="y":
        if answerCharsCapital == " y":
        if answerCharsCapital == "n":

    if answerCharSpecial == "n":  
        if answerCharsCapital == " y":
        if answerCharsCapital == "n":  
    


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*()?"

password =  "".join(random.sample(chars,passlength ))
print (password)
