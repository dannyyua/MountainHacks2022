class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.ready = False

class Guess:
    def __init__(self, playerID, altitude, prominence, isolation):
        self.playerID = playerID
        self.altitude = altitude
        self.prominence = prominence
        self.isolation = isolation

class Mountain:
    def __init__(self, rank, name, altitude, prominence, isolation):
        self.rank = rank
        self.name = name
        self.altitude = altitude
        self.prominence = prominence
        self.isolation = isolation
        