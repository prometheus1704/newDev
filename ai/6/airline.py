class Flight:
    def __init__(self, flight_id, origin, destination, departure_time, arrival_time, cargo_capacity):
        self.flight_id = flight_id
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.cargo_capacity = cargo_capacity  # in kg
        self.cargo_booked = 0

    def is_available(self):
        return self.cargo_booked < self.cargo_capacity

    def book_cargo(self, weight):
        if self.cargo_booked + weight <= self.cargo_capacity:
            self.cargo_booked += weight
            return True
        else:
            return False


class AirlineExpertSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def suggest_flight(self, origin, destination, cargo_weight):
        suggestions = []
        for flight in self.flights:
            if flight.origin == origin and flight.destination == destination:
                if flight.book_cargo(cargo_weight):
                    suggestions.append(flight)
        return suggestions


# Initialize the system and add flights
expert_system = AirlineExpertSystem()

expert_system.add_flight(Flight("AI101", "New York", "London", "08:00", "20:00", 1000))
expert_system.add_flight(Flight("AI102", "New York", "London", "12:00", "00:00", 500))
expert_system.add_flight(Flight("AI103", "New York", "Paris", "10:00", "22:00", 700))

# Ask user for input
origin = input("Enter origin: ")
destination = input("Enter destination: ")
cargo_weight = float(input("Enter cargo weight (kg): "))

# Suggest flights
suggested_flights = expert_system.suggest_flight(origin, destination, cargo_weight)

# Display results
if suggested_flights:
    print("\nSuggested Flights:")
    for f in suggested_flights:
        print(f"Flight ID: {f.flight_id} | Departure: {f.departure_time} | Arrival: {f.arrival_time} | Remaining Capacity: {f.cargo_capacity - f.cargo_booked} kg")
else:
    print("No suitable flights available for your request.")
