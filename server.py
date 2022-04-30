import asyncio
from email.message import Message
import json
from pydoc import cli
import websockets
import game_objects
import game_logic
import score

# connect to this socket with python -m websockets ws://207.23.220.36:8765/

ADDRESS = '142.58.168.251'
PORT = 8765


playerScores = [Score]

clients = set()
roundMountain = [game_objects.Mountain(0,"default",0,0,0)]
players = [game_objects.Player] * 0

async def call(client):
    async for message in client:
        if (client not in clients):
            await connectClient(client)

        try:
            await parseCommand(json.loads(message), client)
        except json.decoder.JSONDecodeError:
            print("No command for: ", message)

async def connectClient(c):
    clients.add(c)
    await sendAll(jsonPlayerCount())

async def addPlayer(msg):
    players.append(game_objects.Player(msg['name']))
    print(players[len(players)-1])

async def addGuess(msg):
    players[msg['playerID']].currentGuess = game_objects.Guess(msg['playerID'], msg['altitude'], msg['prominence'], msg['isolation'])
    print(players[msg['playerID']].currentGuess)

async def sendAll(msg):
    for client in clients:
        await client.send(msg)

async def parseCommand(msg, client):
    command = msg['command']

    if command == 'get_top_scores':
        await sendScore(client)

    if command == 'send_score':
        addScore(client, msg)

    # if (command == 'add_player'):
    #     await addPlayer(msg)

    # if (command == "player_guess"):
    #     await addGuess(msg)
    #     newRound()

async def addScore(client, msg):
    playerScores.append(Score(msg['name'], msg['score']))

async def sendScore(client): 
    scoreJson = {"scores":[{}]}
    for score in playerScores:
        scoreJson["scores"].append({"name":score.name, "scores":score.score})
    await client.send(scoreJson)

def allPlayersReady():
    for player in players:
        if (not player.ready):
            return False
    return True

def listOfGuesses():
    guesses = []
    for player in players:
        guesses.append(player.currentGuess())
    return guesses
    
async def newRound():
    if (allPlayersReady()):
        players = score.gameScores(players, listOfGuesses(), roundMountain)
        roundMountain = game_logic.RandomMountain()
        await sendAll(jsonMountain(roundMountain))

def jsonMountain(mountain):
    return json.dumps({
        "command":"new_mountain",
        "name":mountain.name,
        "altitude":mountain.altitude,
        "prominence":mountain.prominence,
        "isolation":mountain.isolation,
    })

def jsonPlayerCount():
    return json.dumps({
        "command":"player_count",
        "count":len(clients)
    })


async def main():
    async with websockets.serve(call, ADDRESS, PORT):
        await asyncio.Future()  # run forever

asyncio.run(main())