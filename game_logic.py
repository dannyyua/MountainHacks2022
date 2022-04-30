class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.ready = False

class Guess:
    def __init__(self, altitude, avgTemp, avgSnow, hasGondola):
        self.altitude = altitude
        self.avgTemp = avgTemp
        self.avgSnow = avgSnow
        self.hasGondola = hasGondola
