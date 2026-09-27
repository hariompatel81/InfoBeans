# 23. Find the number of cubical boxes of cubical side 3 cm which can be accommodated in carton of dimensions 15 cm × 9 cm × 12 cm. 

cube_side = 3
cube_volume = cube_side * cube_side * cube_side

carton_length = 15
carton_width = 9
carton_height = 12

carton_volume = carton_length * carton_width * carton_height

number_of_box = carton_volume / cube_volume

print(f"The Number of cubical box is : {number_of_box} cm.")