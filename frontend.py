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
from websocket import create_connection
import game_logic
import os

screen_helper = """
ScreenManager:
    HomeScreen:
    JoinScreen:
    LoadScreen:
    PlayScreen:
    MultiScreen:

<HomeScreen>:
    name: 'home'
    # Logo
    Image:
        source: 'logo.png'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.55}
        size_hint: (0.8,0.8)

    # Multiplayer button
    MDFillRoundFlatButton:
        text: 'MULTIPLAYER'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.15}
        on_press: root.manager.current = 'join'

    # Play button
    MDFillRoundFlatButton:
        text: 'SINGLEPLAYER'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.25}
        on_press: root.manager.current = 'play'

<JoinScreen>:
    name: 'join'
    MDToolbar:
        title: 'Join'
        pos_hint: {'top': 1}
        right_action_items: [['account-group']]

    MDTextField:
        id: nickname
        hint_text: 'Enter Your Nickname'
        halign: 'center'
        size_hint_x: 0.4
        pos_hint: {'center_x' : 0.5, 'center_y': 0.7}
        font_size: 22

    MDTextField:
        id: IP
        hint_text: 'Enter IP'
        halign: 'center'
        size_hint_x: 0.4
        pos_hint: {'center_x' : 0.5, 'center_y': 0.5}
        font_size: 22

    MDTextField:
        id: port
        hint_text: 'Enter Port'
        halign: 'center'
        size_hint_x: 0.4
        pos_hint: {'center_x' : 0.5, 'center_y': 0.3}
        font_size: 22

    MDLabel:
        id: IPerror
        text: ''
        halign: 'center'
        size_hint_x: 0.4
        pos_hint: {'center_x' : 0.5, 'center_y': 0.2}
        font_size: 22

    MDFillRoundFlatButton:
        text: 'Back'
        pos_hint: {'center_x' : 0.2,'center_y' : 0.15}
        on_press: root.manager.current = 'home'

    # Start button
    MDRectangleFlatButton:
        text: 'START'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.15}
        on_press: app.Connect()
        

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

<MultiScreen>:
    name: 'multi'
    

"""


class HomeScreen(Screen):
    pass

class JoinScreen(Screen):
    pass

class LoadScreen(Screen):
    pass

class PlayScreen(Screen):
    pass

class MultiScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(JoinScreen(name='join'))
sm.add_widget(LoadScreen(name='load'))
sm.add_widget(PlayScreen(name='play'))
sm.add_widget(MultiScreen(name='multi'))



class MountainApp(MDApp):

    plr = game_logic.Player("Mountain Mike") 

    def build(self):
        screen = Screen()
        self.navigation_bar = Builder.load_string(screen_helper)
        screen.add_widget(self.navigation_bar)
        return screen

    def Connect(self):
        playerName = self.navigation_bar.get_screen('join').ids.nickname.text
        playerIP =  self.navigation_bar.get_screen('join').ids.IP.text
        playerPort = self.navigation_bar.get_screen('join').ids.port.text
        try:
            ws = create_connection("ws://" + str(playerIP) + ":" + str(playerPort) + "/")
            ws.send(playerName)
            self.manager.current = 'load'
        except ValueError or TimeoutError:
            self.navigation_bar.get_screen('join').ids.IPerror.text = "Please Enter a valid IP"
            
        
    

if __name__ == '__main__':
    MountainApp().run()