# 15. Write a java program to accept the cost price of a bike
#     and display the road tax to be paid according to the 
#     following criteria.
#     Cost Price(In Rs)		Tax
#      > 100000			 15%
#      >50000 and <=100000	 10%
#      <=50000			 5%	

bike_price = int(input("Enter cost price :"))
if bike_price > 100000 :
  print(f"Road tax to be paid (15%) : {bike_price*0.15}")
elif bike_price > 50000 and bike_price <= 100000 :
  print(f"Road tax to be paid (10%) : {bike_price*0.10}")
else:
  print(f"Road tax to be paid (5%) : {bike_price*0.05}")
