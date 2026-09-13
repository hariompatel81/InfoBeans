# 37. The surface of the cylinder is 149 cm². The cylinder height is 6 cm. What is the diameter of this cylinder? 

import math

area = 149
height = 6

# cuver surface area of the cylinder = 2 * pi * r * h
# 149 / 2 * pi * h = r

radius = area / (2 * math.pi * height)

diameter = 2 * radius

print(f"The diameter of the cylinder is : {diameter} cm.")
