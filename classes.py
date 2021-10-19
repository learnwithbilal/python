class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = Flight(1)

people = ["Shams", "Osama", "Ritta", "Humam", "Eyhab"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} in the flight successfully!")
    else:
        print(f"No Available Seats for {person}")
