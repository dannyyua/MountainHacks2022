from turtle import pos
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from enum import Enum
import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://142.58.168.251:8765/") as websocket:
        await websocket.send("Hello world!")
        await websocket.recv()


class State(Enum):
    HOME = 0
    JOIN = 1
    WAITING = 2
    PLAYING = 3

class MountainApp(MDApp):

    def retrivePlayer(self):
        print("hi")

    def joinScreen(self, player):
        self.screen.clear()

        self.inputName = MDTextField(
            text = "Enter your nickname: ",
            halign = "center",
            size_hint = (0.8,1),
            pos_hint = {"center_x" : 0.5, "center_y": 0.7},
            font_size = 22
        )
        self.screen.add_widget(self.inputName)

        self.inputIP = MDTextField(
            text = "Enter IP: ",
            halign = "center",
            size_hint = (0.8,1),
            pos_hint = {"center_x" : 0.5, "center_y": 0.5},
            font_size = 22
        )
        self.screen.add_widget(self.inputIP)

        self.inputPort = MDTextField(
            text = "Enter Port: ",
            halign = "center",
            size_hint = (0.8,1),
            pos_hint = {"center_x" : 0.5, "center_y": 0.3},
            font_size = 22
        )
        self.screen.add_widget(self.inputPort)



        
    

    def build(self):
        curState = State.HOME

        playerCount = 2 #TODO
        
        screen = MDScreen()

        # Top Toolbar (Title)
        self.toolbar = MDToolbar(title = "Mountain Guesser")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["android-auto", lambda x : self.activateFan()]]
        screen.add_widget(self.toolbar)

        # Logo
        # screen.add_widget(Image(
        #     source = "logo.png",
        #     pos_hint = {"center_x" : 0.5, "center_y": 0.7}
        #   )
        # )

        

        return screen

if __name__ == '__main__':
    MountainApp().run()