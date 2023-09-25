#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

import math

r = int(input("Enter radius: "))
h = int(input("Enter height: "))

print("The surface area is:", math.pi * r * (r+ math.sqrt(pow(h, 2) + pow(r, 2))))