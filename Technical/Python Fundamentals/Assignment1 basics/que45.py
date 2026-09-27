# 45. Find the sum of 28 terms of an Arithmetic Progression -21 -18 -15 -12 . . . . . 

first_term = -21
common_diffrence = -18 - (-21)
n = 28

# a28 = n/2 * (2*a + (n-1) * d)

sum_of_first_28_terms = n/2 * (2 * first_term + (n-1) * common_diffrence)

print(f"The sum of 28 terms of arithmetic progression : {sum_of_first_28_terms}")