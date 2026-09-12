# 19. A cube with an edge of 7 cm and a cuboid measuring 7 cm × 4 cm × 8 am are kept on a table. Which shape has more volume? 

# Volume of cube is = a * a * a

cube_edge = 7
cube_volume = (cube_edge * cube_edge * cube_edge)
print(f"Cube volume is : {cube_volume} cm\u00b3.")

# Volume of cuboid is = length * width * height

cuboid_length = 7
cuboid_width = 4
cuboid_height = 8

cuboid_volume = cuboid_length * cuboid_width * cuboid_height
print(f"Cuboid volume is : {cuboid_volume} cm\u00b3.")

if cube_volume > cuboid_volume:
  print(f"Cube has {cube_volume - cuboid_volume} cm\u00b3 volume")
else:
  print(f"Cuboid has {cuboid_volume - cube_volume} cm\u00b3 volume")


