# 15. Shelly has a rectangular garden of length 22 m and breadth 15 m. Her friend Rachel has a square garden of side 21 m. Whose garden is bigger and by how much? 

rectangle_length = 20
rectangle_breadth = 15
square_side = 21

# Area of rectangle = length * breadth
area_of_rectangle = rectangle_length * rectangle_breadth

# Area of square = side * side
area_of_square = square_side * square_side

print(f"Area of rectangle is : {area_of_rectangle} m\u00b2")
print(f"Area of square is : {area_of_square} m\u00b2")

if area_of_rectangle > area_of_square:
  print(f"Shelly rectangular garden is bigger by {area_of_rectangle - area_of_square} m\u00b2")
else:
  print(f"Rachel square garden is bigger by {area_of_square - area_of_rectangle} m\u00b2")


