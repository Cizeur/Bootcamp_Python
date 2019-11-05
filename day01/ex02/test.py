from vector import Vector


v1 = Vector([0.0, 1.0, 2.0, 3.0])
v2 = Vector(3)
v3 = Vector((10, 15))
v4 = Vector((11, 16))

print(v1.__dict__)
print(v2.__dict__)
print(v3.__dict__)
print(v4.__dict__)
v5 = v4 + 1
print("add  =>", v5.__dict__)
v5 = 1 + v4
print("radd =>", v5.__dict__)
v5 = v4 + v4
print("addv =>", v5.__dict__)
v5 = v4 - 1
print("sub  =>", v5.__dict__)
v5 = 1 - v4
print("rsub =>", v5.__dict__)
v5 = v4 - v4
print("subv =>", v5.__dict__)
v5 = v4 / 2
print("div  =>", v5.__dict__)
v5 = 2 / v4
print("rdiv =>", v5.__dict__)
v5 = v4 * 2
print("mul  =>", v5.__dict__)
v5 = 2 * v4
print("rmul =>", v5.__dict__)
aa = v4 * v3
print("mulv =>", aa)
print(repr(v5))
print(str(v5))
