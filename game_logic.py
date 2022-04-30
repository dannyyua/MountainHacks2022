class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.ready = False

class Guess:
    def __init__(self, altitude, prominence, isolation):
        self.altitude = altitude
        self.prominence = prominence
        self.isolation = isolation
