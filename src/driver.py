# src/driver.py
# Driver class with location, availability, and earnings tracking

class Driver:
    def __init__(self, driver_id, x, y, name=None, zone=None):
        self.driver_id = driver_id
        self.name = name or f"Driver_{driver_id}"
        self.x = x
        self.y = y
        self.zone = zone
        self.available = True
        self.earnings = 0.0
        self.total_trips = 0
        self.total_distance = 0.0
        self.rating = 5.0
        self.current_location = None  # Can be linked to city location

    def move_to(self, x, y):
        """Move driver to new coordinates"""
        self.x = x
        self.y = y

    def set_location(self, location_name):
        """Set driver's current named location"""
        self.current_location = location_name

    def add_earnings(self, amount):
        """Add to driver's earnings"""
        self.earnings += amount

    def complete_trip(self, distance, fare):
        """Record a completed trip"""
        self.total_trips += 1
        self.total_distance += distance
        self.earnings += fare

    def set_available(self, status):
        """Set driver availability"""
        self.available = status

    def get_utilization(self):
        """Calculate driver utilization rate"""
        if self.total_trips == 0:
            return 0.0
        return self.total_trips

    def to_dict(self):
        """Convert driver to dictionary for serialization"""
        return {
            "driver_id": self.driver_id,
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "zone": self.zone,
            "available": self.available,
            "earnings": round(self.earnings, 2),
            "total_trips": self.total_trips,
            "rating": self.rating
        }

    def __repr__(self):
        status = "Available" if self.available else "Busy"
        return f"Driver({self.driver_id}, {self.name}, {status}, Earnings: ${self.earnings:.2f})"