from typing import final

# returns updated array of Players
def gameScores(playerArr, guessArr, ansMountain):
    for guess in guessArr:
        playerID = guess.playerID
        playerHeight = guess.altitude
        playerProm = guess.prominence
        playerIso = guess.isolation

        #Need to define array of Players
        playerArr[playerID].points += score(playerHeight,playerProm,playerIso,
        ansMountain.altitude,ansMountain.prominence,ansMountain.isolation)

    return(playerArr)



def score(guessHeight, guessProm, guessIso, actualHeight, actualProm, actualIso):
    heightScore = guessHeight/actualHeight
    promScore = guessProm/actualProm
    isoScore = guessIso/actualIso

    tempScores = [heightScore, promScore, isoScore]

    finalScore = 0

    for i in range(0,3):
        
        currScore = tempScores[i]

        tempScores[i] = (1 - abs(1-currScore)) * 10

    for i in range(0,3):
        
        currScore = tempScores[i]

        finalScore += currScore

    finalScore /= 3

    if finalScore > 10 or finalScore < 0:
        finalScore = 0
    

    return(finalScore)

