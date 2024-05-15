
#multiple inheritance

class P1:
    def m1(self):
        print("inside P1 m1")

class P2:
    def m1(self):
        print("inside p2 m1")

class Child(P2,P1):
    pass

ch=Child()
ch.m1()