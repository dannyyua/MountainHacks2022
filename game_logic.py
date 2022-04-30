import random
import game_objects
import csv



def randomLine():
    with open('database.csv') as f:
        next(f)
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
    return chosen_row

def RandomMountain():
    line = randomLine()
    rank = line[0]
    name = line[1]
    altitude = line[2]
    prominence = line[3]
    isolation = line[4]

    return game_objects.Mountain(rank, name, altitude, prominence, isolation)
