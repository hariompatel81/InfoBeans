# 42. Find the Volume of Cylinder whose diameter and height are 2.25cm.

# Cylinder volume = pi * radius**2 * height

import math
diameter = 2.25
radius = diameter/2
height = 2.25

volume = math.pi * (radius**2) * height

print(f"Volume is {volume} cm\u00b3.")