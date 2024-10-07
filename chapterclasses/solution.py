#class
#object --- instnace of a class


# e.g
# Class:Human
# objects:JOhn,Mary,Jack



class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def draw(self):
        print(f"The multiplication of our vars is {self.x * self.y}")

    def __add__(self,test):
        return Point(self.x + test.x , self.y + test.y)

point = Point(1,4)
other = Point(2,4)
combine = point + other
print(combine.y)
print()
print(point.draw())
print(isinstance(point,Point))


class Rectangle:
    def __init__(self): 
        self.length = 1 
        self.width = 1 
    def area(self): 
        return self.length * self.width
    

room_1 = Rectangle()
room_1.length = 10
room_1.width = 15
print("Room 1's area:", room_1.area())
room_3 = Rectangle()
room_3.length = 12
room_3.width = 14
print("Room 3's area:", room_3.area())










# from string import punctuation
# class Analyzer:

#     def __init__(self, s):
#          for c in punctuation:
#               s = s.replace(c,'')
#               s = s.lower()
#               self.words = s.split()
#     def number_of_words(self):
#         return len(self.words)
#     def starts_with(self, s):
#         return len([w for w in self.words if w[:len(s)]==s])
#     def number_with_length(self, n):
#         return len([w for w in self.words if len(w)==n])


