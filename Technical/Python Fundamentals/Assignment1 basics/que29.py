# 29. How many square tiles of side 10 cm will be required to tile a floor measuring 800 cm by 900 cm? 

tiles_side = 10
tiles_area = tiles_side * tiles_side

floor_length = 800
floor_width = 900
floor_area = floor_length * floor_width

number_of_tiles = floor_area / tiles_area

print(f"{number_of_tiles} tiles will be required.")