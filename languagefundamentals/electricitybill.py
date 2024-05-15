
total_consumed_pow= int(input("enter total power consumed"))
# hours_of_use_per_day=int(input("enter total hours used per day"))

# energy_consumed_per_day=(total_consumed_pow*hours_of_use_per_day)/1000
# print(f"energy consumed per day={energy_consumed_per_day}")

electricity_price_per_unit=0.15
total_amount_to_be_paid=total_consumed_pow*0.15

print(f"total bill={total_amount_to_be_paid}")