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


class FlightTicket:
     airline = "Ocean Airlines"
     airline_code= "OA"

     def __init__(self, flight_num=1, airport="JFK", gate="T1-1", time="8:00", seat="1A", passenger="unknown"):
        self.flight_num = flight_num
        self.airport = airport
        self.gate = gate
        self.time = time
        self.seat = seat
        self.passenger = passenger
     def print_info(self):
         print(f"Passenger {self.passenger} departs on flight {self.flight_num} at {self.time} from {self.airport} {self.gate} in {self.seat} ")
    
ticket = FlightTicket(
    flight_num=2121,
    airport="KEF",
    gate="D22B",
    time="11:45",
    seat="12B",
    passenger="Jules Laurent"
)

ticket.print_info()
print(ticket)

