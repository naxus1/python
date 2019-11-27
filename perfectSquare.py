import math

"""
Program that calculate the perfect square
"""
 
print("Enter a number to see if it a perfect square: ", end="")
number = abs(int(input()))
a = math.sqrt(number)
print("Is a sqare {}".format(int(a)))
