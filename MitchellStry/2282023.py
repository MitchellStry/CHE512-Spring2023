import copy
class vector:
    def __init__ (self):
        self.x,self.y=0,0
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def copy (self,other):
        self.x=other.x
        self.y=other.y
    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)
    def show(self):
        print(F"My vector is {self.x}, {self.y}")

v1=vector(1.0,-1.0)
v2=vector(2.0,1.0)
v1.show()
v2.show()
v3=v1+v2
v3.show()
A=vector(1,1)
B=copy.deepcopy(A)
A.show()
B.show()
B.x=-1
B.y=-2
A.show()
B.show()
