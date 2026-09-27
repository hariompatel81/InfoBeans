# 11. The base and height of a triangle are in the ratio 8 : 5 and its area is 320 m². Find the height and base of the triangle.

import math
base_ratio = 8
height_ratio = 5
area = 320

# Area of triangle is 1/2 * base * height
# 1/2 * 8x * 5x = 320
# x = math.sqrt(320 * 2 / 8 * 5)

x = math.sqrt(area * 2 / ( base_ratio * height_ratio))
# print(f"x : {x}")

base = base_ratio * x
height = height_ratio * x

print(f"Base is : {base} m.")
print(f"Height is : {height} m.")
