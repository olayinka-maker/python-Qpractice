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


class Book:
    imprint = "Fantancy Tomes"

    def __init__(self,title="",author="",year=0,pages=0):
        self.title = title
        self.author = author
        self.year = year
        self.pages =pages

    def print_info(self):
        print(f"{self.title} by {self.author} published by Fantasy Tomes in {self.year} with {self.pages}  ")
        print(f"in {self.year} with {self.pages} pages")


book1 = Book(
    title="Lord of the Bracelets",
    author="Blake R. R. Brown",
    year=1999,
    pages=423
)

book2 = Book(
    title="A Match of Thrones",
    author="Terry R. R. Thomas",
    year=2020,
    pages=761
)

book1.print_info()
book2.print_info()

class ProductionCar:
    def __init__(self, make, model, year, max_mph = 0.0):
        self.make = make
        self.model = model
        self.year = year
        self.max_mph = max_mph
    def max_kmh(self):
        return self.max_mph * 1.609344
    def update_max(self, speed):
         self.max_mph = speed

car_1 = ProductionCar('McLaren', 'Speedtail', 2020)
car_1.update_max(250.0)
print(car_1.make, car_1.model, 'reaches', car_1.max_mph, 'mph (',
car_1.max_kmh(), 'km/h)')



class VendngMachine:

    def __init__(self,num):
        self.count = num
        self.max = num

    def refill(self):
        self.count = self.max
        print("Refllled")

    def sell(self,order):
        self.count -=  order
        print(f"Sold: {order}")
    def print_stock(self):
        print(f"Current stock: {self.count}")



