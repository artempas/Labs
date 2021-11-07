from Point3D import Point3D
from Complex import Complex

c1=Complex(1,2)
c2=Complex(2,3)
p1=Point3D(1,2,3)
p2 = Point3D(4,5,6)
print(p1+p2)
print(c1+c2)

print("Complex number keyboard initialization")
x=input("X: ").replace(',','.')
while not x.replace('.','').isdigit():
    print("Only numbers are allowed")
    x = input("X: ")
x=float(x)
y=input("Y: ").replace(',','.')
while not y.replace('.','').isdigit():
    print("Only numbers are allowed")
    y = input("Y: ")
y=float(y)
c3=Complex(x,y)
print(f"{c3},{c3.angle=}")



