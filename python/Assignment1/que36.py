# 36. What is the surface area of a cylinder if the diameter is 15m height is 7m? 

import math

diameter = 15
height = 7
radius = diameter/2

area = 2 * math.pi * radius * (radius + height)

print(f"The surface area of cylinder is : {area} m\u00b2.")