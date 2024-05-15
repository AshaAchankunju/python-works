# 2.	Write a program to calculate the electricity bill. Accept the number of units consumed from the user
# Unit                        Price
# First 100 units      No charge
# Next 100 units     Rs 5 per unit
# After 200 units    Rs 10 per unit
# For example if input unit is 350 then total bill amount is Rs 2000

unit=int(input("enter the no: of unit consumed: "))
if unit<=100:
    total_bill=0
elif unit<=200:
    total_bill=(unit-100)*5
else:
    total_bill=100*5+(unit-200)*10

print("electricty bill= ",total_bill)
