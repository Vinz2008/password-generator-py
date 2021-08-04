#!/usr/bin/python

import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*()?"
passlength = 16
password =  "".join(random.sample(chars,passlength ))
print (password)
