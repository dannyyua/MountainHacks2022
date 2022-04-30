import asyncio
from email.message import Message
import json
from pydoc import cli
import websockets
import game_logic
import score

# connect to this socket with python -m websockets ws://207.23.220.36:8765/

ADDRESS = '207.23.220.36'
PORT = 8765

clients = set()

roundGuesses = set()
roundMountain = [game_logic.Mountain("default",0,0,0)]
players = set()

async def call(client):
    async for message in client:
        if (client not in clients):
            await connectClient(client)

        try:
            await parseCommand(json.loads(message))
        except json.decoder.JSONDecodeError:
            print(message)

async def connectClient(c):
    clients.add(c)
    await sendAll(jsonPlayerCount())

async def addPlayer(msg):
    players.add(game_logic.Player(msg['name']))

async def sendAll(msg):
    for client in clients:
        await client.send(msg)

async def parseCommand(msg):
    command = msg['command']

    if (command == 'add_player'):
        await addPlayer(msg)

    # if (command == "player_guess"):
    #     roundGuesses.append(game_logic.Guess(msg['playerID'], msg['altitude'], msg['prominence'], msg['isolation']))
    #     if (len(roundGuesses) == len(clients)):
    #         players = score.gameScores(players, roundGuesses, roundMountain)
    #         newRound()

# add score to players[playerID]
def calculateGuesses(guesses, mountain):
    pass

def getRandomMountain():
    pass
    
async def newRound():
    roundMountain = getRandomMountain()
    roundGuesses = game_logic.Guess[len(clients)]
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