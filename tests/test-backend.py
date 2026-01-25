from src.ride_share_system import RideShareSystem

system = RideShareSystem()

d1 = system.add_driver(10, 20)
d2 = system.add_driver(50, 60)

r1 = system.add_rider(15, 25)

trip = system.assign_driver(r1)

print("Driver:", trip.driver.driver_id)
print("Fare:", trip.fare)
print("Wait time:", trip.wait_time)

system.complete_trip(trip.driver)
print(system.get_stats())
