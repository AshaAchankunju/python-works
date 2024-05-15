selling_price=int(input("enter selling price:"))
cost_price=int(input("enter cost price"))

profit=selling_price-cost_price
print(f"profit={profit}")
profit_in_perc=(profit/cost_price)*100
print(f"profit in percentage={profit_in_perc}")