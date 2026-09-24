# 30. How many tiles of length 5 cm and breadth 8 cm are needed to tile the floor of a bed room 200 cm long and 400 cm wide? 

tiles_length = 5
tiles_breadth = 8

tiles_area = tiles_length * tiles_breadth

room_long = 200
room_wide = 400

room_area = room_long * room_wide

number_of_tiles = room_area / tiles_area

print(f"{number_of_tiles} tiles are needed to tile the floor of a bad room.")