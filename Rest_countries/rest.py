from json import load

f=open("C:\\Users\\sachi\\OneDrive\Desktop\\my python works\\Rest_countries\\data.json", encoding="utf-8")
data=load(f)
print(len(data))

# all country  names

all_country_names=[c.get("name") for c in data]
# print(all_country_names)

# independent country names

country_names_indep=[c.get("name") for c in data if c.get("independent")==True]
# print(country_names_indep)

# all regions
region={c.get("region") for c in data}  # here we use set comprehension to avoid duplicates
# print(region)

#asian country names
asian_con=[c.get("name") for c in data if c.get("region")=="Asia"]
# print(asian_con)

#print capital of ukraine
cap_uk=[c.get("capital")for c in data if c.get("name")=="Ukraine"]
# print(cap_uk)

#country name and capital
con_nam_capital=[(c.get("name"), c.get("capital")) for c in data]
# print(con_nam_capital)

#print all country name and currencies
for c in data:
    if "currencies" in c:
        currency_data=c.get("currencies")[0]
        # print(currency_data.get("name"),",",c.get("name"))

# india borders
india_border=[c.get("borders")for c in data if c.get("name")=="India"][0]
# print(india_border)

india_border_name=[c.get("name") for c in data if c.get("alpha3Code") in india_border]
# print(india_border_name)

#m country names who having more than 4 borders

for c in data:
   if "borders" in c and len(c.get("borders"))>4:
       print(c.get("name"))

