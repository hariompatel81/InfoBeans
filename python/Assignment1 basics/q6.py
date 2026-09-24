# 6.Find the area of a triangle, sides of which are 10 cm and 9 cm and the perimeter 36 cm. 

# Area of triangle == 1/2(base * heigth)

# Perimeter of triangle == side + base + side

# calculate semi-perimeter(s) s = perimeter/2

# Heron`s formula ==  math.sqrt(s*(s-a)*(s-b)*(s-c))

# Height formula == 2 * (area / base)

import math
side1 = 10
side2 = 9
perimeter = 36

base = perimeter - side1 - side2

s = perimeter/2

area = math.sqrt(s*(s-side1)*(s-base)*(s-side2))

height = 2 * (area / base)

print(f"Area of triangle : {area} cm\u00b2 ")

#print(f"Base : {base} cm.")
#print(f"S : {s} cm.")
#print(f"Height : {height:.2f} cm.")

