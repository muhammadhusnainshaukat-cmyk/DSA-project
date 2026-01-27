# src/rider.py
# Rider class with pickup and drop-off points

class Rider:
    def __init__(self, rider_id, x, y, name=None):
        self.rider_id = rider_id
        self.name = name or f"Rider_{rider_id}"
        self.x = x  # Pickup x coordinate
        self.y = y  # Pickup y coordinate
        self.pickup_location = None  # Named location
        self.dropoff_location = None
        self.dropoff_x = None
        self.dropoff_y = None
        self.total_trips = 0
        self.total_spent = 0.0

    def set_pickup(self, location_name, x=None, y=None):
        """Set pickup location"""
        self.pickup_location = location_name
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def set_dropoff(self, location_name, x=None, y=None):
        """Set dropoff location"""
        self.dropoff_location = location_name
        if x is not None:
            self.dropoff_x = x
        if y is not None:
            self.dropoff_y = y

    def complete_trip(self, fare):
        """Record a completed trip"""
        self.total_trips += 1
        self.total_spent += fare

    def to_dict(self):
        """Convert rider to dictionary"""
        return {
            "rider_id": self.rider_id,
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "pickup_location": self.pickup_location,
            "dropoff_location": self.dropoff_location,
            "total_trips": self.total_trips,
            "total_spent": round(self.total_spent, 2)
        }

    def __repr__(self):
        return f"Rider({self.rider_id}, {self.name}, Trips: {self.total_trips})"