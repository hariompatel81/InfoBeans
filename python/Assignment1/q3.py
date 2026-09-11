# 3. How many tiles whose length and breadth are 13 cm and 7 cm respectively are needed to cover a rectangular region whose length and breadth are 520 cm and 140 cm?

tiles_length = 13
tiles_breadth = 7

tiles_area = tiles_length * tiles_breadth

rectangular_region_length = 520
rectangular_region_breadth = 140

rectangular_region_area = rectangular_region_length * rectangular_region_breadth

tiles_count = rectangular_region_area / tiles_area

print(f"{tiles_count} tiles are respectively needed.")
