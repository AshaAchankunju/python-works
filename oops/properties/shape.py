

class Shape:
    name:str

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name
    
class Rectangle(Shape):
    l:int
    b:int

    def __init__(self, name,l,b):
        super().__init__(name)
        self.l=l
        self.b=b

    def area(self):
        result=self.l*self.b
        print(result)

class Circle(Shape):
    r:int

    def __init__(self, name,r):
        super().__init__(name)
        self.r=r

    def carea(self):
        result=3.14*self.r**2
        print(result)

recobj=Rectangle("rectangle",10,5)
recobj.area()

circleobj=Circle("circle",5)
circleobj.carea()