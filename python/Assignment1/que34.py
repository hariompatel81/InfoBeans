# 34. A wooded area is in the shape of a a trapezoid whose bases measure 128 m and 92 m and its height is 40 m. A 4 m wide walkway is constructed which runs perpendicular to the two bases. Calculate the area of the wooded area after the addition of the walkway. 

wooded_area_base1 = 128
wooded_area_base2 = 92
wooded_area_height = 40

# Area of trapezoid = 1/2 * (base1 + base2) * height
area_of_wooded_area = 1/2 * ((wooded_area_base1 + wooded_area_base2)) * wooded_area_height

walkway_width = 4
# area of rectengle = length * width
walkway_area = wooded_area_height * walkway_width

rest_wooded_area = area_of_wooded_area - walkway_area

print(f"Area of wooded area after addition of the walkway is : {rest_wooded_area} m\u00b2.")