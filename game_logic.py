import random

def Randomline():

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
    
