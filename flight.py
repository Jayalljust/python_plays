#some OOP basics
class Flight():
    def __init__ (self, capacity):
        self.capacity = capacity
        self.passengers = []
    
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(2)

people = ["Seva", "Dima", "Tema"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfullly.")
    else:
        print(f"There is no place to seat for {person}")