import random
import game_objects
from ssl import ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION
from unicodedata import name

def randomLine():

    filesize = 51
    offset = random.randrange(filesize)

    f = open("database.csv")
    f.seek(offset)
    f.readline()
    random_line = f.readline()

    if len(random_line) == 0:
        f.seek(0)
        random_line = f.readline()

    return random_line

def RandomMountain():
    line = randomLine().split(",")
    rank = line[0]
    name = line[1].split("[")[0]
    altitude = line[4].strip('"').split(" ")[0]
    prominence = line[5].strip('"').split(" ")[0]
    isolation = line[6].strip('"')
    return game_objects.Mountain(rank, name, altitude, prominence, isolation)
