import numpy
class Matrix:
    def __init__(self,args):
        self.m=len(args)
        self.n=len(args[0])
        self.args=args
        self.size=(self.m,self.n)
        self.numpy_array=numpy.array(self.args)
        for row in args:
            if len(row)!=self.n:
                print('This is not a matrix')
                return
    def __add__(self,other):
        if isinstance(other,Matrix):
            if self.size!=other.size:
                print('This addition is not available.')
                return
            return Matrix(self.numpy_array+other.numpy_array)
        
    def __iadd__(self,other):
        return self+other
    def __sub__(self,other):
        if self.size!=other.size:
            print('This subtraction is not available.')
            return
        return Matrix(self.numpy_array-other.numpy_array)
    def __isub__(self,other):
        return self-other
    def allint(self):
        all_int=True
        for row in self.args:
            for value in row:
                if not isinstance(value,int):
                    all_int=False
        return all_int
    def det(self):
        det_value=numpy.linalg.det(self.numpy_array)
        if self.allint():
            det_value=round(det_value)
        return det_value
    def inv(self):
        inverse_value=numpy.linalg.inv(self.numpy_array)
        return Matrix(inverse_value)
    def transpose(self):
        return Matrix(self.numpy_array.transpose())
    def __mul__(self,other):
        if isinstance(other,Matrix):
            if self.n!=other.m:
                print('This multiplying is not available.')
                return
            return Matrix(self.numpy_array@other.numpy_array)
        else:
            return Matrix(self.numpy_array*other)
    def __rmul__(self,other):
        return self*other
    def __imul__(self,other):
        return self*other

def eye(n):
    return Matrix(numpy.eye(n))
a=numpy.array([
    [1,2]
])
a*=2
print(a)