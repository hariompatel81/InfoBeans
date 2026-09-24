# 41. I need to calculate the cylinder volume with a height of 50 cm and a diameter of 30 cm. 

import math
height = 50
diameter = 30
radius = diameter/2

# cylinder volime = pi * r**2 * h
volume = math.pi * radius**2 * height

print(f"Cylinder volume : {volume}cm\u00b3")