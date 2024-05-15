class Mobile:
    name:str
    Brand:str
    display:str
    price: int

    def __init__(self,name,Brand,display,price):
        self.name=name
        self.Brand=Brand
        self.display=display
        self.price=price

    def display_mobiles(self):
        print(self.name,self.price)

    def __str__(self):
        return self.name

obj=Mobile("samsung","s23","gfhd",253625)
obj.display_mobiles()
print(obj)
