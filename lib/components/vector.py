import math
class Vector:
    def __init__(self,x:float,y:float):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __iadd__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    def __isub__(self,other):
        return Vector(self.x-other.x,self.y-other.y)
    def __mul__(self,other):
        if isinstance(other,Vector):
            return self.x*other.x+self.y*other.y
        else:
            return Vector(self.x*other,self.y*other)
    def __rmul__(self,other):
        return Vector(self.x*other,self.y*other)
    def __imul__(self,other):
        return Vector(self.x*other,self.y*other)
    def __truediv__(self,other):
        return Vector(self.x/other,self.y/other)
    def __rtruediv__(self,other):
        return Vector(self.x/other,self.y/other)
    def __itruediv__(self,other):
        return Vector(self.x/other,self.y/other)
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
    def __ne__(self,other):
        return self.x!=other.x or self.y!=other.y
    def abs(self):
        return (self.x**2+self.y**2)**0.5
    def __gt__(self,other):
        return self.abs()>other.abs()
    def __lt__(self,other):
        return self.abs()<other.abs()
    def __ge__(self,other):
        return self.abs()>=other.abs()
    def __le__(self,other):
        return self.abs()<=other.abs()
    def tup(self):
        return (self.x,self.y)
    def deg(self):
        return math.degrees(math.atan2(self.y,self.x))