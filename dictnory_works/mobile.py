mobile={"id":100,"name":"iphone15","price":1000000,"imei":2345,"processor":"apple"}
# print all key value pairs
for m,n in mobile.items():
    print(m,n)

# print Name
print (mobile.get("name"))

# print price
print(mobile.get("price"))

# update price as rs 85000
mobile.update({"price":85000})
print(mobile)

# remove imei
mobile.pop("imei")
print(mobile)

mobile["offer"]=1000
print(mobile)

mobile["price"]+=1000
print(mobile) # to add 1000 to the existing price of the mobile

print("color" in mobile)