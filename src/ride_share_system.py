from src.driver import Driver
from src.rider import Rider
from src.trip import Trip
from src.dispatch_engine import DispatchEngine


class RideShareSystem:
    def __init__(self):
        self.drivers = []
        self.riders = []
        self.trips = []
        self.dispatcher = DispatchEngine()
        self.total_wait_time = 0
        self.total_earnings = 0

    def add_driver(self, x, y):
        d = Driver(len(self.drivers)+1, x, y)
        self.drivers.append(d)
        return d

    def add_rider(self, x, y):
        r = Rider(len(self.riders)+1, x, y)
        self.riders.append(r)
        return r

    def assign_driver(self, rider):
        driver, distance = self.dispatcher.find_nearest_driver(self.drivers, rider)

        if not driver:
            return None

        wait_time = distance / 10
        fare = distance * 5

        driver.available = False
        driver.earnings += fare
        driver.move_to(rider.x, rider.y)

        trip = Trip(driver, rider, distance, fare, wait_time)
        self.trips.append(trip)

        self.total_wait_time += wait_time
        self.total_earnings += fare

        return trip

    def complete_trip(self, driver):
        driver.available = True

    def get_stats(self):
        if len(self.trips) == 0:
            return {
                "trips": 0,
                "avg_wait": 0,
                "total_earnings": 0
            }

        return {
            "trips": len(self.trips),
            "avg_wait": round(self.total_wait_time / len(self.trips), 2),
            "total_earnings": round(self.total_earnings, 2)
        }
