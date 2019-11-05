class Vector:
    
    def __init__(self, val=[]):
        if not val:
            raise Exception("Please give non empty initialisation values")
        if isinstance(val, list):
            try: 
                self.values = list(map(float, val))
            except Exception:
                raise Exception("List elems should be convertible to float")
        elif isinstance(val, int) and val > 0:
            self.values = list(map(float, range(val)))
        elif isinstance(val, tuple):
            assert len(val) == 2, "Invalid tuple size should be 2 ints"
            try: 
                self.values = list(map(float, range(val[0], val[1])))
            except Exception:
                raise Exception("Invalid tuple not made of 2 int")
        else:
            raise Exception("Invalid initialisation parameter")
        self.size = len(self.values)
        assert self.size > 0,  "Size should be superior to zero"

    def __add__(self, val):
        if isinstance(val, int):
            val = float(val)
        if isinstance(val, float):
            return Vector([x + val for x in self.values])
        elif isinstance(val, Vector):
            assert val.size == self.size, "Vector should have the same size"
            zipped = list(zip(self.values, val.values))
            return Vector([x[0] + x[1] for x in zipped])
        else:
            raise Exception("Unmanaged operation for this type")

    def __radd__(self, val):
        return self.__add__(val)

    def __mul__(self, val):
        if isinstance(val, int):
            val = float(val)
        if isinstance(val, float):
            return Vector([x * val for x in self.values])
        elif isinstance(val, Vector):
            assert val.size == self.size, "Vector should have the same size"
            zipped = list(zip(self.values, val.values))
            scal_prod = sum([x[0] * x[1] for x in zipped])
            return scal_prod
        else:
            raise Exception("Unmanaged operation for this type")
    
    def __rmul__(self, val):
        return self.__mul__(val)
    
    def __sub__(self, val):
        if isinstance(val, int):
            val = float(val)
        if isinstance(val, float):
            return Vector([x - val for x in self.values])
        elif isinstance(val, Vector):
            assert val.size == self.size, "Vector should have the same size"
            zipped = list(zip(self.values, val.values))
            return Vector([x[0] - x[1] for x in zipped])
        else:
            raise Exception("Unmanaged operation for this type")

    def __rsub__(self, val):
        if isinstance(val, int):
            val = float(val)
        if isinstance(val, float):
            return Vector([val - x for x in self.values])
        elif isinstance(val, Vector):
            assert val.size == self.size, "Vector should have the same size"
            zipped = list(zip(self.values, val.values))
            return Vector([x[1] - x[0] for x in zipped])
        else:
            raise Exception("Unmanaged operation for this type")

    def __truediv__(self, div):
        if isinstance(div, int):
            div = float(div)
        if isinstance(div, float):
            assert div, "Invalid division by zero"
            return Vector([x / div for x in self.values])
        else:
            raise Exception("Unmanaged operation for this type")
    
    def __rtruediv__(self, div):
        if isinstance(div, int):
            div = float(div)
        if isinstance(div, float):
            try:
                return Vector([div / x for x in self.values])
            except ZeroDivisionError:
                raise ZeroDivisionError("One of the vector value is zero")
        else:
            raise Exception("Unmanaged operation for this type")

    def __str__(self):
        return ("Vector [" 
               + ", ".join(list(map(str, self.values))) 
               + "] of size : " + str(self.size))
    
    def __repr__(self):
        return ("< Instance of Vector class: [" 
                + ", ".join(list(map(str, self.values))) 
                + "]{" + str(self.size) 
                + "} >" )
