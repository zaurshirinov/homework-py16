
# PYTHON CLASSES HOMEWORK ASSIGNMENT
# =====================================

# OBJECTIVE: Learn Python classes through interactive examples with planes and passengers
# DIFFICULTY: Progressive (Beginner to Intermediate)
# TOTAL TASKS: 30

# === PART 1: BASIC CLASS CONCEPTS (Tasks 1-10) ===

# Task 1: Create a simple class called 'Person' with:
# - __init__ method that takes name and age parameters
# - Store name and age as instance variables using self
# - Create an instance of Person with your name and age
# - Print the person's name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old")


person = Person("Zaur", 19)

print(person.name)
print(person.age)

person.introduce()

# Task 2: Add a method called 'introduce' to the Person class that:
# - Prints "Hi, I'm [name] and I'm [age] years old"
# - Create a Person instance and call the introduce method


# Task 3: Create a class called 'Car' with:
# - __init__ method taking brand, model, and year
# - A method called 'start_engine' that prints "The [brand] [model] engine is running"
# - Create a Car instance and call start_engine
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.brand} {self.model} engine is running")
    
    def get_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}"
    

car = Car("Toyota", "Corolla", 2022)
car.start_engine()
print(car.get_info())

# Task 4: Add a method called 'get_info' to the Car class that:
# - Returns a string with all car information
# - Test it by creating a car and printing the result of get_info()


# Task 5: Create a class called 'Book' with:
# - __init__ method for title, author, and pages
# - A method called 'read' that prints "Reading [title] by [author]"
# - A method called 'is_long' that returns True if pages > 300, False otherwise
# - Test all methods
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Reading {self.title} by {self.author}")

    def is_long(self):
        return self.pages > 300
    
book = Book("I", "Shirinov Zaur", 303)
print(book.author)

book.read()
print(book.is_long())

# Task 6: Create a class called 'Student' with:
# - __init__ method for name, student_id, and grade
# - A method called 'study' that prints "[name] is studying"
# - A method called 'get_grade' that returns the grade
# - Create 3 different students and test all methods
class Student:
    def __init__(self, name: str, student_id: int, grade: int) -> None:
        self.name = name
        self.student_id = student_id
        self.grade = grade

    def study(self) -> None:
        print(f"{self.name} is studying")

    def get_grade(self) -> int:
        return self.grade
    
    def promote(self) -> None:
        self.grade += 1
        print(f"{self.name} was promoted to grade {self.grade}")

    

leyla = Student("Leyla", 1044377, 60)
zaur = Student("Zaur", 1044477, 90)
vasif = Student("Vasif", 1043234, 50)

print(vasif.grade)
print(zaur.student_id)

leyla.study()
vasif.promote()

# Task 7: Add a method called 'promote' to the Student class that:
# - Increases the grade by 1
# - Prints "[name] was promoted to grade [new_grade]"
# - Test with a student

# Task 8: Create a class called 'BankAccount' with:
# - __init__ method for account_holder and initial_balance (default 0)
# - A method called 'deposit' that adds money to balance
# - A method called 'withdraw' that subtracts money from balance
# - A method called 'get_balance' that returns current balance
# - Test all methods

class BankAccount:
    def __init__(self, account_holder: str, initial_balance: int =0) -> None:
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance:_.1f}")

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance:_.1f}")

    def get_balance(self) -> float:
        return f"{self.balance:_f}"

account = BankAccount("Zaur", 700_000_000)
account.withdraw(500_000)
account.deposit(40_000_000)
print(account.get_balance())

# Task 9: Add validation to the BankAccount withdraw method:
# - Check if withdrawal amount is greater than balance
# - If yes, print "Insufficient funds" and don't withdraw
# - If no, proceed with withdrawal
# - Test with valid and invalid withdrawal attempts

# Task 10: Create a class called 'Rectangle' with:
# - __init__ method for width and height
# - A method called 'area' that returns width * height
# - A method called 'perimeter' that returns 2 * (width + height)
# - A method called 'is_square' that returns True if width equals height
# - Test all methods

class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def is_square(self) -> bool:
        return self.width == self.height
    
rect1 = Rectangle(5, 3)
rect2 = Rectangle(4, 4)

print(rect1.area())        # 15
print(rect1.perimeter())   # 16
print(rect1.is_square())   # false

print(rect2.area())        # 16
print(rect2.perimeter())   # 16
print(rect2.is_square())   # true

# === PART 2: INTERMEDIATE CLASS CONCEPTS (Tasks 11-20) ===

# Task 11: Create a class called 'Airplane' with:
# - __init__ method for airline, flight_number, and max_passengers
# - Instance variables: current_passengers (starts at 0), destination
# - A method called 'board_passenger' that increases current_passengers by 1
# - A method called 'get_passenger_count' that returns current_passengers
# - Test by creating an airplane and boarding 5 passengers

# Task 12: Add validation to the Airplane board_passenger method:
# - Check if current_passengers < max_passengers
# - If yes, board the passenger and print "Passenger boarded. Total: [count]"
# - If no, print "Airplane is full! Cannot board more passengers"
# - Test with boarding more passengers than the maximum

# Task 13: Add a method called 'takeoff' to the Airplane class that:
# - Checks if current_passengers > 0
# - If yes, prints "Flight [flight_number] taking off to [destination] with [count] passengers"
# - If no, prints "Cannot takeoff - no passengers on board"
# - Test both scenarios

# Task 14: Create a class called 'Passenger' with:
# - __init__ method for name, age, and seat_number
# - A method called 'board_plane' that prints "[name] is boarding seat [seat_number]"
# - A method called 'is_adult' that returns True if age >= 18, False otherwise
# - Create 3 passengers and test all methods

# Task 15: Add a method called 'get_ticket_info' to the Passenger class that:
# - Returns a formatted string with passenger details
# - Include name, age, seat number, and adult status
# - Test with different passengers

# Task 16: Modify the Airplane class to work with Passenger objects:
# - Change board_passenger to accept a Passenger object
# - Print the passenger's name and seat when boarding
# - Update the takeoff method to show passenger names
# - Test by creating passengers and boarding them

# Task 17: Add a method called 'list_passengers' to the Airplane class that:
# - Prints all boarded passengers' information
# - If no passengers, prints "No passengers on board"
# - Test with empty and occupied airplane

# Task 18: Create a class called 'Flight' that manages an Airplane and its Passengers:
# - __init__ method takes airline, flight_number, destination, max_passengers
# - Create an Airplane instance inside Flight
# - Methods: add_passenger, takeoff, get_status
# - Test by creating a flight and adding passengers

# Task 19: Add validation to the Flight add_passenger method:
# - Check if passenger is already on the flight (by name)
# - Check if airplane has space
# - If both checks pass, add passenger and return True
# - If not, return False with appropriate message
# - Test with duplicate passengers and full airplane

# Task 20: Add a method called 'emergency_landing' to the Flight class that:
# - Prints "EMERGENCY LANDING! All passengers must evacuate!"
# - Resets passenger count to 0
# - Prints "Flight [flight_number] has landed safely"
# - Test the emergency landing

# === PART 3: ADVANCED CLASS CONCEPTS (Tasks 21-30) ===

# Task 21: Create a class called 'Airport' that manages multiple Flights:
# - __init__ method for airport_name
# - Instance variable: flights (empty list)
# - Methods: add_flight, remove_flight, list_flights
# - Test by creating an airport and adding multiple flights

# Task 22: Add a method called 'find_flight' to the Airport class that:
# - Takes a flight_number as parameter
# - Returns the Flight object if found, None if not found
# - Test by searching for existing and non-existing flights

# Task 23: Add a method called 'get_flight_status' to the Airport class that:
# - Takes a flight_number and returns detailed flight information
# - Include passenger count, destination, and flight status
# - Handle case where flight doesn't exist
# - Test with different flights

# Task 24: Create a class called 'Pilot' with:
# - __init__ method for name, license_number, and flight_hours
# - Methods: fly_plane, get_experience_level
# - Experience levels: "Junior" (< 1000 hours), "Senior" (1000-5000), "Captain" (> 5000)
# - Test with pilots of different experience levels
    
# Task 25: Modify the Flight class to include a Pilot:
# - Add pilot parameter to __init__
# - Add method called 'assign_pilot' that assigns a pilot to the flight
# - Modify takeoff to include pilot information
# - Test by creating flights with different pilots


# Task 26: Add a method called 'calculate_fuel_needed' to the Flight class that:
# - Takes distance as parameter
# - Calculates fuel needed based on passenger count and distance
# - Formula: (passenger_count * 0.1) + (distance * 0.05)
# - Return the fuel amount needed
# - Test with different passenger counts and distances

# Task 27: Create a class called 'CrewMember' with:
# - __init__ method for name, position (pilot, flight_attendant, engineer)
# - Methods: work, get_position_info
# - Add validation to ensure position is one of the valid options
# - Test with different crew members

# Task 28: Modify the Flight class to support multiple crew members:
# - Change pilot to crew_members (list)
# - Add methods: add_crew_member, remove_crew_member, list_crew
# - Add validation to ensure at least one pilot is assigned
# - Test by adding different crew members

# Task 29: Add a method called 'flight_safety_check' to the Flight class that:
# - Checks if there's at least one pilot
# - Checks if passenger count doesn't exceed maximum
# - Checks if all crew members are valid
# - Returns True if all checks pass, False otherwise
# - Print detailed results of each check
# - Test with valid and invalid flight configurations

# Task 30: Create a comprehensive test scenario:
# - Create an airport
# - Create a flight with destination "New York", max 150 passengers
# - Create 5 passengers with different ages and seat numbers
# - Create 3 crew members (1 pilot, 2 flight attendants)
# - Add all passengers and crew to the flight
# - Perform safety check
# - If safe, take off the flight
# - Print final flight status
# - Test both safe and unsafe scenarios

# === BONUS CHALLENGES ===

# Bonus 1: Add a method to calculate flight cost based on distance and passenger count
# Bonus 2: Create a method to simulate flight delays and their impact
# Bonus 3: Add weather conditions that affect flight safety
# Bonus 4: Create a method to generate flight reports with statistics
# Bonus 5: Implement a simple booking system with seat selection

# === EVALUATION CRITERIA ===
# - Correct use of __init__ and self
# - Proper method definitions and calls
# - Appropriate use of instance variables
# - Implementation of validation logic
# - Clean, readable code structure
# - Proper error handling
# - Creative problem-solving

# Good luck with your Python classes journey! 🚀✈️
class Passenger:
    def __init__(
        self,
        name: str,
        age: int,
        seat_number: int
    ) -> None:
        self.name = name
        self.age = age
        self.seat_number = seat_number

    def board_plane(self) -> None:
        print(f"{self.name} is boarding seat {self.seat_number}")

    def is_adult(self) -> bool:
        return  self.age >= 18 
    
    def get_ticket_info(self) -> str:
        status = "Adult" if self.is_adult() else "Child"
        return (
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Seat: {self.seat_number}, "
            f"Status: {status}"
        )


class Airplane:
    def __init__(
        self,
        airline: str,
        flight_number: str,
        max_passengers: int,
        destination: str,
        distance: int 
    ) -> None:
        self.airline = airline
        self.flight_number = flight_number
        self.max_passengers = max_passengers
        self.destination = destination
        self.passengers: list[Passenger] = []
        self.distance = distance
        self.booked_seats: set[int] = set()

    def board_passenger(self, passenger: Passenger) -> None:
        # Bonus 5)
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)
            print(f"{passenger.name} boarded seat {passenger.seat_number}")
        else:
            print("Airplane is full! Cannot board more passengers")

    def book_seat(self, passenger: Passenger) -> bool:
        if passenger.seat_number in self.booked_seats:
            print(f"Seat {passenger.seat_number} is already booked")
            return False

        if len(self.passengers) >= self.max_passengers:
            print("Airplane is full! Cannot book more seats")
            return False

        self.booked_seats.add(passenger.seat_number)
        self.passengers.append(passenger)
        print(f"Seat {passenger.seat_number} booked for {passenger.name}")
        return True

    def get_passenger_count(self) -> int:
        return len(self.passengers)
    
    def takeoff(self) -> None:
        if self.passengers:
            names = ", ".join(p.name for p in self.passengers)
            print(
                f"Flight {self.flight_number} taking off to "
                f"{self.destination} with passengers: {names}"
            )
        else:
            print("Cannot takeoff - no passengers on board")

    def list_passengers(self) -> None:
        if not self.passengers:
            print("No passengers on board")
        else:
            for passenger in self.passengers:
                print(passenger.get_ticket_info())
            

class Pilot:
    def __init__(
        self, 
        name: str, 
        license_number: str, 
        flight_hours: int
    ) -> None:
        self.name = name
        self.license_number = license_number
        self.flight_hours = flight_hours

    def fly_plane(self):
        print(f"{self.name} is flying the plane")

    def get_experience_level(self):
        if self.flight_hours < 1000:
            return "Junior"
        elif self.flight_hours <= 5000:
            return "Senior"
        else:
            return "Captain"
            

class Flight:
    def __init__(
        self, 
        airline: str,
        flight_number: str, 
        destination: str, 
        max_passengers: int,
        distance: int
    ) -> None:
        self.airplane = Airplane(
            airline=airline,
            flight_number=flight_number,
            max_passengers=max_passengers,
            destination=destination,
            distance=distance
        )
        self.crew_members: list[CrewMember] = []
        self.delay_minutes = 0
        self.delay_reason = None
        self.status = "Scheduled"
        self.weather = "Clear"
    
    def add_crew_member(self, crew_member: 'CrewMember') -> None:
        self.crew_members.append(crew_member)
        print(f"{crew_member.name} ({crew_member.position}) added to flight {self.airplane.flight_number}")

    def remove_crew_member(self, name: str) -> None:
        for cm in self.crew_members:
            if cm.name == name:
                self.crew_members.remove(cm)
                print(f"{name} removed from flight {self.airplane.flight_number}")
                return
        print(f"{name} not found in flight {self.airplane.flight_number}")

    def list_crew(self) -> None:
        if not self.crew_members:
            print(f"No crew members on flight {self.airplane.flight_number}")
        else:
            for cm in self.crew_members:
                print(f"{cm.name} - {cm.position}")

    def add_passenger(self, passenger: Passenger ) -> bool:
        for p in self.airplane.passengers:
            if p.name == passenger.name:
                print(f"Error: {passenger.name} is already on this flight")
                return False
        
        # Use seat booking instead of direct boarding
        return self.airplane.book_seat(passenger)

    def takeoff(self) -> None:
        pilots = [cm for cm in self.crew_members if cm.position == "pilot"]
        if not pilots:
            print("Cannot take off - no pilot assigned")
            return
        pilot = pilots[0]
        print(f"Pilot {pilot.name} is in command")

        if self.weather in ["Storm", "Extreme Wind"]:
            print(f"Cannot take off due to unsafe weather: {self.weather}")
            return
        
        if not self.airplane.passengers:
            print("Cannot takeoff - no passengers on board")
            return
        
        self.airplane.takeoff()

    def get_status(self) -> str:
        return (
            f"Flight {self.airplane.flight_number} to {self.airplane.destination} | "
            f"Passengers: {self.airplane.get_passenger_count()}/"
            f"{self.airplane.max_passengers}"
        )   
    
    def calculate_fuel_needed(self) -> float:
        passenger_count = self.airplane.get_passenger_count()
        distance = self.airplane.distance
        fuel_needed = (passenger_count * 0.1) + (distance * 0.05)
        return fuel_needed

    def emergency_landing(self) -> None:
        if self.airplane.passengers:
            print("EMERGENCY LANDING! All passengers must evacuate!")
            self.airplane.passengers.clear()
        else:
            print("EMERGENCY LANDING! No passengers on board to evacuate.")
        print(f"Flight {self.airplane.flight_number} has landed safely")

    def flight_safety_check(self) -> bool:
        print(f"Performing safety check for flight {self.airplane.flight_number}...")

        pilots = [cm for cm in self.crew_members if cm.position == "pilot"]
        if not pilots:
            print("Safety Check Failed: No pilot assigned")
            pilot_ok = False
        else:
            print(f"Safety Check Passed: Pilot assigned ({pilots[0].name})")
            pilot_ok = True

        passenger_count = self.airplane.get_passenger_count()
        if passenger_count > self.airplane.max_passengers:
            print(f"Safety Check Failed: Passenger count {passenger_count} exceeds maximum {self.airplane.max_passengers}")
            passenger_ok = False
        else:
            print(f"Safety Check Passed: Passenger count {passenger_count}/{self.airplane.max_passengers}")
            passenger_ok = True

        crew_valid = True
        for cm in self.crew_members:
            if cm.position not in CrewMember.VALID_POSITIONS:
                print(f"Safety Check Failed: Invalid crew member position {cm.position} for {cm.name}")
                crew_valid = False
        if crew_valid:
            print("Safety Check Passed: All crew members are valid")

        if self.weather in ["Storm", "Extreme Wind"]:
            print(f"Safety Check Failed: Unsafe weather ({self.weather})")
            weather_ok = False
        else:
            print(f"Safety Check Passed: Weather is {self.weather}")
            weather_ok = True


        all_ok = pilot_ok and passenger_ok and crew_valid and weather_ok
        print(f"Overall Flight Safety: {'PASS' if all_ok else 'FAIL'}\n")
        return all_ok
    
    # Bonus 1: 
    def calculate_flight_cost(self) -> float:
        fuel_needed = self.calculate_fuel_needed()

        fuel_price_per_unit = 2.5
        total_cost = fuel_needed * fuel_price_per_unit
        return f"{total_cost}$"
    
    # Bonus 2:
    def simulate_delay(self, minutes: int, reason: str) -> None:
        self.delay_minutes += minutes
        self.delay_reason = reason

        if self.delay_minutes > 0:
            self.status = "Delayed"

        print(
            f"Flight {self.airplane.flight_number} delayed by "
            f"{minutes} minutes due to {reason}."
        )

    def get_delay_impact(self) -> None:
        if self.delay_minutes == 0:
            print("No delays for this flight")
            return

        extra_cost = self.delay_minutes * 20 

        print(
            f"Delay Impact:\n"
            f"- Total delay: {self.delay_minutes} minutes\n"
            f"- Reason: {self.delay_reason}\n"
            f"- Extra cost: {extra_cost}$"
        )

    # Bonus 3:
    def set_weather(self, condition: str) -> None:
        self.weather = condition
        print(f"Weather set to {condition} for flight {self.airplane.flight_number}")

    # Bonus 4:
    def generate_flight_report(self) -> str:
        safety_ok = self.flight_safety_check()
        passenger_count = self.airplane.get_passenger_count()
        fuel_needed = self.calculate_fuel_needed()
        flight_cost = self.calculate_flight_cost()

        pilots = [cm for cm in self.crew_members if cm.position == "pilot"]
        pilot_name = pilots[0].name if pilots else "Not assigned"

        report = (
            f"\n===== FLIGHT REPORT =====\n"
            f"Flight Number: {self.airplane.flight_number}\n"
            f"Destination: {self.airplane.destination}\n"
            f"Status: {'READY FOR TAKEOFF' if safety_ok else 'FLIGHT NOT ALLOWED'}\n"
            f"Weather: {self.weather}\n"
            f"Pilot: {pilot_name}\n"
            f"Crew Members: {len(self.crew_members)}\n"
            f"Passengers: {passenger_count}/{self.airplane.max_passengers}\n"
            f"Fuel Needed: {fuel_needed}\n"
            f"Flight Cost: {flight_cost}\n"
        )

        if self.delay_minutes > 0:
            report += (
                f"Delay: {self.delay_minutes} minutes\n"
                f"Delay Reason: {self.delay_reason}\n"
            )
        else:
            report += "Delay: None\n"

        report += "==========================\n"
        return report

    
           

class Airport:
    def __init__(self, airport_name: str) -> None:
        self.airport_name = airport_name
        self.flights: list[Flight] = []

    def add_flight(self, flight: Flight) -> None:
        for f in self.flights:
            if f.airplane.flight_number == flight.airplane.flight_number:
                print(
                    f"Flight {flight.airplane.flight_number} already exists at "
                    f"{self.airport_name}"
                )
                return

        self.flights.append(flight)
        print(
            f"Flight {flight.airplane.flight_number} added to "
            f"{self.airport_name}"
        )

    def remove_flight(self, flight_number: str) -> None:
        for flight in self.flights:
            if flight.airplane.flight_number == flight_number:
                self.flights.remove(flight)
                print(
                    f"Flight {flight_number} removed from "
                    f"{self.airport_name}"
                )
                return

        print(f"Flight {flight_number} not found at {self.airport_name}")

    def list_flights(self) -> None:
        if not self.flights:
            print(f"No flights at {self.airport_name}")
        else:
            print(f"Flights at {self.airport_name}:")
            for flight in self.flights:
                print(flight.get_status())
    
    def find_flight(self, flight_number: str) -> Flight | None:
        for flight in self.flights:
            if flight.airplane.flight_number == flight_number:
                return flight
        return None
    
    def get_flight_status(self, flight_number: str) -> str:
        flight = self.find_flight(flight_number)

        if flight is None:
            return f"Flight {flight_number} not found at {self.airport_name}"
        

        pilots = [cm for cm in flight.crew_members if cm.position == "pilot"]
        pilot_info = f"Pilot: {pilots[0].name}" if pilots else "Pilot: Not assigned"

        return (
            f"Airport: {self.airport_name}\n"
            f"Flight Number: {flight.airplane.flight_number}\n"
            f"Destination: {flight.airplane.destination}\n"
            f"Passengers: {flight.airplane.get_passenger_count()}/"
            f"{flight.airplane.max_passengers}\n"
            f"{pilot_info}"
        )


class CrewMember:
    VALID_POSITIONS = {"pilot", "flight_attendant", "engineer"}

    def __init__(self, name: str, position: str) -> None:
        if position not in self.VALID_POSITIONS:
            raise ValueError(
                f"Invalid position: {position}. "
                f"Valid positions are: {', '.join(self.VALID_POSITIONS)}"
            )

        self.name = name
        self.position = position

    def work(self) -> None:
        print(f"{self.name} is working as a {self.position}")

    def get_position_info(self) -> str:
        return f"{self.name} - Position: {self.position}"

if __name__ == "__main__":
    airport = Airport("Haydar Aliyev International Airport")
    flight_1 = Flight("AZAL", "ZB-3172", "New York", 180, 10000)

    passenger_list = [
        Passenger("Zaur", 19, 11),
        Passenger("Lale", 10, 10),
        Passenger("Nur", 20, 9),
        Passenger("Leyla", 11, 12),
        Passenger("Fuad", 32, 18),
        Passenger("Kamal", 21, 14),
        Passenger("Messi", 29, 88),
        Passenger("Maqa", 20, 8),
        Passenger("Neymar", 23, 128)
    ]


    crews = [
        CrewMember("Vusal", "pilot"),
        CrewMember("Lamiye", "flight_attendant"),
        CrewMember("Vasif", "flight_attendant")
    ]

    for p in passenger_list:
        flight_1.add_passenger(p)

    for c in crews:
        flight_1.add_crew_member(c)
    
    print("\n")

    flight_1.set_weather("Clear")

    flight_1.flight_safety_check()
    flight_1.takeoff()
    print(flight_1.get_status())

    print(flight_1.calculate_flight_cost())
    print(flight_1.calculate_fuel_needed())

    # flight_1.simulate_delay(45, "Bad weather")
    # flight_1.get_delay_impact()
    # print(flight_1.generate_flight_report())

