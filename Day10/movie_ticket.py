# ------------------------------
# Movie Ticket Booking System
# ------------------------------

# Base Class
class Show:
    def __init__(self, base_price):
        self.base_price = base_price

    # polymorphic method
    def calculate_price(self):
        return self.base_price


# Child Class (2D Show)
class TwoDShow(Show):
    def calculate_price(self):
        return self.base_price   # no extra charge


# Child Class (3D Show)
class ThreeDShow(Show):
    def calculate_price(self):
        return self.base_price + 100   # 3D glass charge


# Movie Class
class Movie:
    def __init__(self, name, show_type):
        self.name = name
        self.show_type = show_type    # object of 2D or 3D show

    def show_details(self):
        print(f"Movie: {self.name}, Price: ₹{self.show_type.calculate_price()}")


# Theatre Class (encapsulation for seats)
class Theatre:
    def __init__(self, name, total_seats):
        self.name = name
        self.__available_seats = total_seats   # private variable

    def book_seat(self):
        if self.__available_seats > 0:
            self.__available_seats -= 1
            return True
        return False


# Customer Class
class Customer:
    def __init__(self, name, mobile):
        self.name = name
        self.mobile = mobile


# Ticket Class
class Ticket:
    def __init__(self, movie, customer, seat_no):
        self.movie = movie
        self.customer = customer
        self.seat_no = seat_no
        self.price = movie.show_type.calculate_price()

    def show_ticket(self):
        print("\n----- Ticket -----")
        print(f"Customer: {self.customer.name}")
        print(f"Movie: {self.movie.name}")
        print(f"Seat No: {self.seat_no}")
        print(f"Price: ₹{self.price}")
        print("------------------")

    # operator overloading
    def __add__(self, other):
        return self.price + other.price

    # static method
    @staticmethod
    def validate_seat(seat_no):
        return seat_no > 0


# ------------------------------
# Main Program Flow
# ------------------------------

movie = Movie("Kalki", ThreeDShow(300))  # 3D movie
theatre = Theatre("PVR", 50)
customer = Customer("Babu", "9999988888")

seat_no = 10

# Validate seat
if Ticket.validate_seat(seat_no):

    # Check seat availability
    if theatre.book_seat():
        ticket1 = Ticket(movie, customer, seat_no)
        ticket1.show_ticket()
    else:
        print("No seats available!")
else:
    print("Invalid seat number")
