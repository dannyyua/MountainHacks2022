class Player:
    currGuess = 99
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.ready = False
    def __str__(self):
        return 'Player(name='+ str(self.name) + ", points=" + str(self.points) + ", isReady=" + str(self.ready) + ")"

class Guess:
    def __init__(self, playerID, altitude, prominence, isolation):
        self.playerID = playerID
        self.altitude = altitude
        self.prominence = prominence
        self.isolation = isolation
    def __str__(self):
        return 'Guess(playerID='+ str(self.playerID) + ", altitude=" + str(self.altitude) + ", prominence=" + str(self.prominence) + ", isolation=" + str(self.isolation) + ")"

    def updateReady(self, playerArr):
        playerArr[self.playerID].ready = True
        return(playerArr)

class Mountain:
    def __init__(self, rank, name, altitude, prominence, isolation):
        self.rank = rank
        self.name = name
        self.altitude = altitude
        self.prominence = prominence
        self.isolation = isolation
    def __str__(self):
        return 'Mountain(rank='+ str(self.rank) + ", name=" + str(self.name) + ", altitude=" + str(self.altitude) + ", prominence=" + str(self.prominence) + ", isolation=" + str(self.isolation) + ")"

class Score:
    def __init__(self, name, score):
        self.name = name
        self.points = score