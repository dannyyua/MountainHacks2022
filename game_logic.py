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
    name = line[1].split("[")[0]
    altitude = line[4].strip('"').split(" ")[0].split(".")[0]
    prominence = line[5].strip('"').split(" ")[0].split(".")[0]
    isolation = line[6].strip('"').replace(",","").split(" ")[0].split(".")[0]

    return game_objects.Mountain(rank, name, altitude, prominence, isolation)
