import kivy
from turtle import pos
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton, MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from enum import Enum
import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://142.58.168.251:8765/") as websocket:
        await websocket.send("Player_name,")
        await websocket.recv()


screen_helper = """
ScreenManager:
    HomeScreen:
    JoinScreen:
    LoadScreen:
    PlayScreen:

<HomeScreen>:
    name: 'home'
    # Logo
    Image:
        source: 'logo.png'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.55}
        size_hint: (0.8,0.8)

    # Play button
    MDFillRoundFlatButton:
        text: 'PLAY'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.3}
        on_press: root.manager.current = 'join'

<JoinScreen>:
    name: 'join'
    MDToolbar:
        title: 'Join'
        pos_hint: {'top': 1}

    MDTextField:
        hint_text: 'Enter Your Nickname'
        halign: 'center'
        size_hint_x: 0.4
        pos_hint: {'center_x' : 0.5, 'center_y': 0.7}
        font_size: 22
    
    MDTextField:
        hint_text: 'Enter IP'
        halign: 'center'
        size_hint_x: 0.4
        pos_hint: {'center_x' : 0.5, 'center_y': 0.5}
        font_size: 22

    MDTextField:
        hint_text: 'Enter Port'
        halign: 'center'
        size_hint_x: 0.4
        pos_hint: {'center_x' : 0.5, 'center_y': 0.3}
        font_size: 22
    
    MDFillRoundFlatButton:
        text: 'Back'
        pos_hint: {'center_x' : 0.2,'center_y' : 0.15}
        on_press: root.manager.current = 'home'

    # Start button
    MDRectangleFlatButton:
        text: 'START'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.15}
        on_press: root.manager.current = 'join'

<LoadScreen>:
    name: 'load'
    MDLabel:
        text: 'Upload'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu'
        
<PLayScreen>:
    name: 'play'
    

"""


class HomeScreen(Screen):
    pass

class JoinScreen(Screen):
    pass

class LoadScreen(Screen):
    pass

class PlayScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(JoinScreen(name='join'))
sm.add_widget(LoadScreen(name='load'))
sm.add_widget(LoadScreen(name='play'))

class MountainApp(MDApp):


    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

if __name__ == '__main__':
    MountainApp().run()