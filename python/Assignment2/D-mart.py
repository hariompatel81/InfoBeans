"""A person enter in a D-Mart mall for the shopping. He is first
time visiting the D-mart mall. 
He/She has to purchase 10 items.

System should ask for the name of the customer and Gender.

User will tell you the item name and quantity of each product
purchased one by one.

You have to calculate the total bill amount on the following 
Criteria basis
 
 on first product purchase if quantitiy greater then
 4 then you have to offer 5% discount on total price of that product
 
 on 5th product purchase you have to offer 10% discount on total
 price.
 
 on 10th product purchase you have to offer 15% discount on total
 price of that product. 

 let suppose the cost of 1st product is 10
 cost of 2nd product is 20
    .
    .
 cost of 10th product is 100;

 if Total Bill amount is greater then 10000 then you have
 to offer 15% of total bill amount
 if total Bill amount is between 5000 and 10000 then 
 you have to offer 10% of total bill amount
 
 Also 10% GST of total Bill Amount
 
 Then you have to ask for carry bag to customer
 if he/she yes then add 10 rupees in total bill amount.
 
 if the customer is female then you have to gift a Cadeberry
 If the customer is mael then you have to gift a Ladger Wallet
 
 Develop a Java Application to Generate the Bill in 
 Following Format
 
                         D-Mart
   Name : Cheeku Sing			Data: 12/9/2022
   -----------------------------------------------------------
   Item Name	Quantity    Price	Total   After-Discount		                      
     Item-1	   5	      10        50 Rs       47.5 Rs
     Item-2	   3	      20	60 RS       60.0 RS	
       .
       .
       .
       .
       .
       .
       .
     Item-10	  20        100         2000       300.0 Rs
   ----------------------------------------------------------
                                        A.P	    D.P	
                                        45000	    43500 
     Gift :- Cadeberry                  0.00	    0.00
                                        
     Carry Bag : yes                    10:00	    10:00
     GST (10%)	                        450         450
   ---------------------------------------------------------
                                        45460       43960 RS
                                        
                       Thank You
                        To Vist
                         D-Mart                 
                                          		  
   ---------------------------------------------------------- 
"""


customer_name = input("Enter customer name :")
customer_gender = input("Enter customer gender :")
date = input("Enter date :")

#1st product
product1_name = input("Enter product1 name :")
product1_quantity = int(input("Enter product1 quantity :"))
product1_cost = int(input("Enter product1 cost :"))

#2nd product
product2_name = input("Enter product2 name :")
product2_quantity = int(input("Enter product2 quantity :"))
product2_cost = int(input("Enter product2 cost :"))

#3rd product
product3_name = input("Enter product3 name :")
product3_quantity = int(input("Enter product3 quantity :"))
product3_cost = int(input("Enter product3 cost :"))

#4th product
product4_name = input("Enter product4 name :")
product4_quantity = int(input("Enter product4 quantity :"))
product4_cost = int(input("Enter product4 cost :"))

#5th product
product5_name = input("Enter product5 name :")
product5_quantity = int(input("Enter product5 quantity :"))
product5_cost = int(input("Enter product5 cost :"))

#6th product
product6_name = input("Enter product6 name :")
product6_quantity = int(input("Enter product6 quantity :"))
product6_cost = int(input("Enter product6 cost :"))

#7th product
product7_name = input("Enter product7 name :")
product7_quantity = int(input("Enter product7 quantity :"))
product7_cost = int(input("Enter product7 cost :"))

#8th product
product8_name = input("Enter product8 name :")
product8_quantity = int(input("Enter product8 quantity :"))
product8_cost = int(input("Enter product8 cost :"))

#9th product
product9_name = input("Enter product9 name :")
product9_quantity = int(input("Enter product9 quantity :"))
product9_cost = int(input("Enter product9 cost :"))

#10th product
product10_name = input("Enter product10 name :")
product10_quantity = int(input("Enter product10 quantity :"))
product10_cost = int(input("Enter product10 cost :"))

#  on first product purchase if quantitiy greater then 4 then you have to offer 5% discount on total price of that product

product1_item_total_price = product1_quantity * product1_cost
product1_item_total_price_with_discount = product1_item_total_price
if product1_quantity > 4:
  product1_item_total_price_with_discount = product1_item_total_price - (product1_item_total_price * 0.05)

#  on 5th product purchase you have to offer 10% discount on total price.
product5_item_total_price = product5_quantity * product5_cost
product5_item_total_price_with_discount = product5_item_total_price - (product5_item_total_price * 0.10)

#  on 10th product purchase you have to offer 15% discount on total price of that product.
product10_item_total_price = product10_quantity * product10_cost
product10_item_total_price_with_discount = product10_item_total_price - (product10_item_total_price * 0.15)

product2_item_total_price = product2_quantity * product2_cost

product3_item_total_price = product3_quantity * product3_cost

product4_item_total_price = product4_quantity * product4_cost

product6_item_total_price = product6_quantity * product6_cost

product7_item_total_price = product7_quantity * product7_cost

product8_item_total_price = product8_quantity * product8_cost

product9_item_total_price = product9_quantity * product9_cost


products_total_price = product1_quantity * product1_cost + product2_item_total_price + product3_item_total_price + product4_item_total_price + product5_item_total_price + product6_item_total_price + product7_item_total_price + product8_item_total_price + product9_item_total_price + product10_item_total_price

products_total_price_with_discount = product1_item_total_price_with_discount + product2_item_total_price + product3_item_total_price + product4_item_total_price + product5_item_total_price_with_discount + product6_item_total_price + product7_item_total_price + product8_item_total_price + product9_item_total_price + product10_item_total_price_with_discount

products_total_price_after_discount = products_total_price
if products_total_price_with_discount > 10000 :
  products_total_price_after_discount = products_total_price_with_discount - (products_total_price_with_discount * 0.15)
elif products_total_price_with_discount > 5000 and products_total_price_with_discount < 10000 :
  products_total_price_after_discount = products_total_price_with_discount - (products_total_price_with_discount * 0.10)

gst_on_total_bill = products_total_price * 0.10

carry_bag = input("Are you want to carry bag (yes/no):")
print("\n\n")

carry_bag_price = 10
final_bill = products_total_price_after_discount + gst_on_total_bill
if carry_bag == "yes":
  final_bill = products_total_price_with_discount + gst_on_total_bill + 10
else:
  carry_bag_price = 0.00

products_total_price_with_gst_bag = products_total_price + gst_on_total_bill + carry_bag_price
 
gift = ""
if customer_gender == "female":
  gift = "Cadeberry"
else:
  gift = "Ladger Wallet"


print("   \t\t\t    D-mart")
print(f"   Name : {customer_name}\t\t\t Date: {date}")
print("   ------------------------------------------------------------")
print("   Item Name     Quantity     Print     Total     After-Discount")
print(f"      {product1_name}          {product1_quantity}         {product1_cost}         {product1_item_total_price} Rs         {product1_item_total_price_with_discount} Rs")
print(f"      {product2_name}          {product2_quantity}         {product2_cost}         {product2_item_total_price} Rs          {product2_item_total_price} Rs")       
print(f"      {product3_name}          {product3_quantity}         {product3_cost}         {product3_item_total_price} Rs          {product3_item_total_price} Rs")
print(f"      {product4_name}          {product4_quantity}         {product4_cost}         {product4_item_total_price} Rs          {product4_item_total_price} Rs")
print(f"      {product5_name}          {product5_quantity}         {product5_cost}         {product5_item_total_price} Rs        {product5_item_total_price_with_discount} Rs")
print(f"      {product6_name}          {product6_quantity}         {product6_cost}         {product6_item_total_price} Rs          {product6_item_total_price} Rs")
print(f"      {product7_name}          {product7_quantity}         {product7_cost}         {product7_item_total_price} Rs          {product7_item_total_price} Rs")
print(f"      {product8_name}          {product8_quantity}         {product8_cost}         {product8_item_total_price} Rs          {product8_item_total_price} Rs")
print(f"      {product9_name}          {product9_quantity}         {product9_cost}         {product9_item_total_price} Rs          {product9_item_total_price} Rs")
print(f"      {product10_name}          {product10_quantity}         {product10_cost}           {product10_item_total_price} Rs          {product10_item_total_price_with_discount} Rs")
print("   --------------------------------------------------------------------------")
print("                                              A.P        D.P")
print(f"                                              {products_total_price}     {products_total_price_with_discount}")
print(f"   Gift :- {gift}                         0.00      0.00\n")
print(f"   Carry Bag : {carry_bag}                             {carry_bag_price}       {carry_bag_price}")
print(f"   GST (10%)                                   {gst_on_total_bill}        {gst_on_total_bill}")
print("   --------------------------------------------------------------------------")
print(f"                                         {products_total_price_with_gst_bag}        {final_bill} Rs")
print("\n")
print("                              Thank You")
print("                               To Vist")
print("                                D-Mart")
print("\n")
print("   --------------------------------------------------------------------------")


