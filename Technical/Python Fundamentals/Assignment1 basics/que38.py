# 38. The cylinder has a volume of 1287. The base has a radius 10. What is the area of the surface of the cylinder? 

import math

volume = 1287
radius = 10

# cylinder_volume = pi * radius**2 * height

height = volume / (math.pi * (radius**2))
print(height)

# area of the surface of the cylinder = 2*pi*r(r+h)

area = 2 * math.pi * radius * (radius + height)

print(f"The area of the surface of the cylinder is : {area}")