import math

class DispatchEngine:
    def find_nearest_driver(self, drivers, rider):
        nearest = None
        min_dist = float("inf")

        for d in drivers:
            if d.available:
                dist = math.dist((d.x, d.y), (rider.x, rider.y))
                if dist < min_dist:
                    min_dist = dist
                    nearest = d

        return nearest, min_dist
