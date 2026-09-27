# 26. How many bricks will be required to lay a path 120 m long and 2.4 m breadth if a brick is 24 cm long and 15 cm wide? 

brick_length = 24
brick_width = 15

brick_area = brick_length * brick_width

path_length = 12000
path_width = 240

path_area = path_length * path_width

number_of_brick = path_area / brick_area

print(f"{number_of_brick} bricks are required.")