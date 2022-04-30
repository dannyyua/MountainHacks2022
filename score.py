
from typing import final


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
    
    

    print(finalScore)

score(10,20,79,10,20,30)

