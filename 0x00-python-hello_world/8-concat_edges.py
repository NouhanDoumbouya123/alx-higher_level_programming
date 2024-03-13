#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# YOUR CODE 
print((lambda s: s[39:67] + s[107:112] + s[0:7])(s := "Python is an interpreted, interactive, object-oriented programming language that combines remarkable power with very clear syntax"))
#print(str)
