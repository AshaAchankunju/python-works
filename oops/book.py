class Book:
    name:str
    author:str
    pages:int
    price:int

    def __init__(self,name,author,pages,price):
        self.name=name
        self.author=author
        self.pages=pages
        self.price=price

    def display(self):
        print(self.name,self.author)

    def __str__(self):
        return self.name

obj=Book("abc","mt",124,145)
obj.display()
print(obj)