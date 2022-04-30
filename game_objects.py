class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.ready = False
    def __str__(self):
        return 'Player(name='+ str(self.name) + ", points=" + self.points + ", isReady=" + self.ready + ")"

class Guess:
    def __init__(self, playerID, altitude, prominence, isolation):
        self.playerID = playerID
        self.altitude = altitude
        self.prominence = prominence
        self.isolation = isolation
    def __str__(self):
        return 'Guess(playerID='+ str(self.playerID) + ", altitude=" + self.altitude + ", prominence=" + self.prominence + ", isolation=" + self.isolation + ")"

class Mountain:
    def __init__(self, rank, name, altitude, prominence, isolation):
        self.rank = rank
        self.name = name
        self.altitude = altitude
        self.prominence = prominence
        self.isolation = isolation
    def __str__(self):
        return 'Mountain(rank='+ str(self.rank) + ", name=" + self.name + ", altitude=" + self.altitude + ", prominence=" + self.prominence + ", isolation=" + self.isolation + ")"

        