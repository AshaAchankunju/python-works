from json import load
f=open("C:\\Users\\sachi\\OneDrive\\Desktop\\my python works\\products\\items.json",encoding="utf-8")
data=load(f)
print(len(data))

categories={p.get("category")for p in data}
print(categories)

electronics_prod=[p for p in data if p.get("category")=="electronics"]
print(len(electronics_prod))

jewelery_prod=[p for p in data if p.get("category")=="jewelery"]
print(len(jewelery_prod))   