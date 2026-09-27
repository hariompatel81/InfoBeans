# 21. A brick measures 15 cm in length, 8 cm in breadth and 5 cm in height. How many bricks will be used to make a wall of length 15 m, breadth 10 m and height 8 metres? 

brick_length = 15
brick_breadth = 8
brick_height = 5

brick_volume = brick_length * brick_breadth * brick_height

wall_length = 15
wall_breadth = 10
wall_height = 8

wall_volume = wall_length * wall_breadth * wall_height * 1000000

number_of_bricks = wall_volume / brick_volume

print(f"{number_of_bricks} bricks will need to make wall.")

