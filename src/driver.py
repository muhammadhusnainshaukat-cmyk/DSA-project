class Driver:
    def __init__(self, driver_id, x, y):
        self.driver_id = driver_id
        self.x = x
        self.y = y
        self.available = True
        self.earnings = 0

    def move_to(self, x, y):
        self.x = x
        self.y = y
