# 12. Find the area of a right angled triangle whose hypotenuse is 13 cm and one of its sides containing the right angle is 12 cm. Find the length of the other side.

import math
hypotenuse = 13
side1 = 12

# Through pythagoream theorem hypotenuse**2 = side1**2 + side2**2

side2 = math.sqrt(hypotenuse ** 2 - side1 ** 2)

# Area of triangle = 1/2 * base * height

area = 1/2 * side1 * side2

print(f"Area of right angle triangle is : {area} cm\u00b2")
print(f"Side : {side2} cm.")



