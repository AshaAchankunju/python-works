product={"code":1001, "name":"orange","price":35}
# print(product["price"])

for k in product.keys(): # return all keys
    print(k)

for v in product.values(): # return all values
    print(v)

for ke, va in product.items(): # return all key value pairs
    print(ke,va)

print(product.get("price")) # to get the value of a key
print(product.get("prices")) # if there is no such key it will return none and continue the remaining program

product["price"]=50  # to update a dictionary
print(product) 

product.update({"name":"oranges"}) # to update a dictionary
print(product)

product.pop("price")
print(product)