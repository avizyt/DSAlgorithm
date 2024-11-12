class Point:
    x: int
    y: int

    __match_arg__ = ["x", "y"]
    def __init__(self,x,y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        case Point(x=0, y=0 ):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Something else")
        case _: print("Not a point")

p = Point(0,2)

where_is(p)
print(p.x)