# 39. Find the surface of the cylinder if its diameter is 12 centimeters and its height is 9 centimeters. 

import math
diameter = 12
radius = diameter/2
height = 9

# Surface area of the cylinder is = 2*pi*r(r+h)

area = 2 * math.pi * radius * (radius + height)

print(f"The surface area of the cylinder : {area}")