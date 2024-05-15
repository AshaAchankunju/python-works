class parent:
    def mobile(self):
        print("redmi 12")
    
    def vehicle(self):
        print("splender")

class Child(parent):
    def mobile(self):
        print("iphone 12")

ch=Child()
ch.mobile()
ch.vehicle()