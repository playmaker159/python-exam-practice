class point:
    x=0
    y=0
p=point()
def print_point(pt):
    pt.x=10
    print(pt.x)

print_point(p)
print(p.x)