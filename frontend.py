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
import game_objects
import os
from kivy.properties import StringProperty

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
        multiline: False

    MDTextField:
        id: IP
        hint_text: 'Enter IP'
        halign: 'center'
        size_hint_x: 0.4
        pos_hint: {'center_x' : 0.5, 'center_y': 0.5}
        font_size: 22
        multiline: False

    MDTextField:
        id: port
        hint_text: 'Enter Port'
        halign: 'center'
        size_hint_x: 0.4
        pos_hint: {'center_x' : 0.5, 'center_y': 0.3}
        font_size: 22
        multiline: False

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

    MDToolbar:
        title: root.currentRound
        pos_hint: {'top': 1}
        right_action_items: [['exit-to-app', lambda x : app.set_screen('home')]]
        left_action_items: [['android-auto']]

    Image:
        source: root.imageName
        pos_hint: {'center_x' : 0.5, 'center_y': 0.5}
        size_hint: (0.8,0.8)
    
    MDLabel:
        markup: True
        text: '[b]'+root.mountainName+'[/b]'
        halign: 'center'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.85}
        font_size: 30
        color: (1, 0, 1, 0.5)
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
    rounds = 0
    max_rounds = 5
    

    mountain = game_logic.RandomMountain()
    #imageName = StringProperty(str(mountain.rank) + ".png")
    imageName = StringProperty("logo.png")


    mountainName = StringProperty(str(mountain.name))
    currentRound = StringProperty("Round " + str(rounds) + "/" + str(max_rounds))

class MultiScreen(Screen):
    pass




class MountainApp(MDApp):
    
    # Create the screen manager
    sm = ScreenManager()
    sm.add_widget(HomeScreen(name='home'))
    sm.add_widget(JoinScreen(name='join'))
    sm.add_widget(LoadScreen(name='load'))
    sm.add_widget(PlayScreen(name='play'))
    sm.add_widget(MultiScreen(name='multi'))

    plr = game_objects.Player("Mountain Mike") 

    def build(self):
        screen = Screen()
        self.navigation_bar = Builder.load_string(screen_helper)
        screen.add_widget(self.navigation_bar)
        return screen

    
    def set_screen(self, screen_name):
        self.navigation_bar.current = screen_name  



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