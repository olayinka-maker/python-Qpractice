#class
#object --- instnace of a class


# e.g
# Class:Human
# objects:JOhn,Mary,Jack



class Point: 

    def __init__(self,x,y) -> None:
        pass

    def draw(self):
        print("draw")

point = Point()
print(isinstance(point,Point))