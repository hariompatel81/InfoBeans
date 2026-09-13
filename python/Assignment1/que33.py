# 33. A rectangular garden has dimensions of 30 m by 20 m and is divided in to 4 parts by two pathways that run perpendicular from its sides. One pathway has a width of 3 m and the other, 4 m. Calculate the total usable area of the garden. 

garden_length = 30
garden_width = 20

# step 1. area of garden
garden_area = garden_length * garden_width

# step 2. pathway 1 area
pathway1_width = 3
pathway1_area = garden_width * pathway1_width

#step 3. pathway 2 area
pathway2_width = 4 
pathway2_area = garden_length * pathway2_width

#step 4. overlaping area
overlapping_area = pathway1_width * pathway2_width

#step 5. usable area = garden_area - (pathway1_area + pathway2_area - overlapping_area)
usable_area = garden_area - (pathway1_area + pathway2_area - overlapping_area)

print(f"Usable area is : {usable_area} m\u00b2.")