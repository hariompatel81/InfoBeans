# 43. Find the cost of polishing the base of a cone whose height is 4cm and slant height 5 cm at the rate of 10 rs. Per sq. cm 

# r = math.sqrt(slant_height**2 - height**2)

import math
height = 4
slant_height = 5

radius = math.sqrt(slant_height**2 - height**2)

base_area = math.pi * (radius**2)

cost = base_area * 10

print(f"The cost of polishing the base of cone is :{cost}")

