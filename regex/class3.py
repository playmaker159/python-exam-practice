import copy
class point:
    x=0
    y=5
p1=point()
p1.x=10
p2=copy.copy(p1)
p2.x=20
print(p1.x==p2.x)
print(point.x)