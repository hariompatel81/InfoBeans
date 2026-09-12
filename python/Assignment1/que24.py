# 24. How many bricks each 25 cm long, 10 cm wide and 7.5 cm thick will be required for a wall 20 m long, 2 m high and 0.75 m thick? If bricks sell at $900 per thousand what will it cost to build the wall? 

brick_length = 25
brick_width = 10
brick_height = 7.5

brick_volume = brick_length * brick_width * brick_height

wall_length = 2000
wall_width = 200
wall_height = 75

wall_volume = wall_length * wall_width * wall_height

number_of_bricks = wall_volume / brick_volume

cost_of_wall = (number_of_bricks / 1000) * 900

print(f"Cost of wall is : ${cost_of_wall}.")

