
class Cuisine:
    name:str

    def __init__(self, name):
        self.name=name

class Dish(Cuisine):
    dish_name:str
    ingredints:str
    price:int

    def __init__(self, name,dish_name,ingredints,price):
        super().__init__(name)
        self.dish_name=dish_name
        self.ingredints=ingredints
        self.price=price
    
    def __str__(self):
        return self.name

dishobj=Dish("italian","noodles","schewzwan",1542)
print(dishobj)

