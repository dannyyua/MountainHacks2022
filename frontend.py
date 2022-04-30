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
from kivy.uix.gridlayout import GridLayout
from enum import Enum
from websocket import create_connection
import game_logic
import game_objects
import os
import score
from kivy.properties import StringProperty

screen_helper = """
ScreenManager:
    HomeScreen:
    JoinScreen:
    LoadScreen:
    EndingScreen:
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
    #TODO

<EndingScreen>:
    name: 'ending'
    MDRectangleFlatButton:
        text: 'RETURN'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.1}
        on_press: app.resetGame()
    MDLabel:
        markup: True
        text: '[u][b]'+"CONGRATULATIONS"+'[/b][/u]'
        halign: 'center'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.65}
        font_size: 60
        color: (0, 0.29, 1, 1)
    MDLabel:
        text: "Your Final Score is..."
        halign: 'center'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.5}
        font_size: 30
        color: (0, 0.29, 1, 1)
    MDLabel:
        id: finalScore
        markup: True
        text: ''
        halign: 'center'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.4}
        font_size: 30
        color: (0, 0.29, 1, 1)

        
<PLayScreen>:
    name: 'play'

    MDToolbar:
        title: root.currentRound
        pos_hint: {'top': 1}
        right_action_items: [['exit-to-app', lambda x : app.resetGame()]]
        left_action_items: [['android-auto']]

    Image:
        source: root.imageName
        pos_hint: {'center_x' : 0.5, 'center_y': 0.55}
        size_hint: (0.5,0.5)
    
    MDLabel:
        markup: True
        text: '[b]'+root.mountainName+'[/b]'
        halign: 'center'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.85}
        font_size: 30
        color: (0, 0.29, 1, 1)

    MDLabel:
        markup: True
        text: '[u]' + 'Current Score' +'[/u]'
        halign: 'right'
        pos_hint: {'center_x' : 0.49, 'center_y': 0.80}
        font_size: 30
        color: (1, 0, 1, 0.5)

    MDLabel:
        text: root.currentScore
        halign: 'right'
        pos_hint: {'center_x' : 0.49, 'center_y': 0.72}
        font_size: 30
        color: (0, 0.29, 1, 1)

    MDLabel:
        text: "Guess This Mountain's..."
        halign: 'center'
        pos_hint: {'center_x' : 0.5, 'center_y': 0.25}
        font_size: 30
        color: (0, 0.29, 1, 1)

    MDTextField:
        id: altitude
        hint_text: 'Altitude'
        helper_text: 'Height of the mountain'
        helper_text_mode: 'on_focus'
        halign: 'center'
        size_hint_x: 0.2
        pos_hint: {'center_x' : 0.2, 'center_y': 0.14}
        font_size: 22
        multiline: False

    MDTextField:
        id: prominence
        hint_text: 'Prominence'
        helper_text: 'Relative height of peaks'
        helper_text_mode: 'on_focus'
        halign: 'center'
        size_hint_x: 0.2
        pos_hint: {'center_x' : 0.5, 'center_y': 0.14}
        font_size: 22
        multiline: False

    MDTextField:
        id: isolation
        hint_text: 'Isolation'
        helper_text: 'Distance to nearest mountain'
        helper_text_mode: 'on_focus'
        halign: 'center'
        size_hint_x: 0.2
        pos_hint: {'center_x' : 0.8, 'center_y': 0.14}
        font_size: 22
        multiline: False
        # Submit button

    MDRectangleFlatButton:
        text: 'SUBMIT'
        pos_hint: {'center_x' : 0.89, 'center_y': 0.25}
        on_press: app.processGuess()
    
    MDLabel:
        id: valueError
        text: ''
        halign: 'center'
        size_hint_x: 0.4
        pos_hint: {'center_x' : 0.5, 'center_y': 0.05}
        font_size: 22
        color: (1,0,0,1)

        
    
<MultiScreen>:
    name: 'multi'



"""


class HomeScreen(Screen):
    pass

class JoinScreen(Screen):
    pass

class LoadScreen(Screen):
    pass

class EndingScreen(Screen):
    pass


class PlayScreen(Screen):
    rounds = 1
    maxRounds = 5
    score = 0
    maxScore = 0

    mountain = game_logic.RandomMountain()
    imageName = StringProperty("images/" + str(mountain.rank) + ".jpg")


    mountainName = StringProperty(str(mountain.name))
    currentRound = StringProperty("Round " + str(rounds) + "/" + str(maxRounds))
    currentScore = StringProperty(str(score) + "/" + str(maxScore))

class MultiScreen(Screen):
    pass



class MountainApp(MDApp):
    
    # Create the screen manager
    sm = ScreenManager()
    sm.add_widget(HomeScreen(name='home'))
    sm.add_widget(JoinScreen(name='join'))
    sm.add_widget(LoadScreen(name='load'))
    sm.add_widget(EndingScreen(name='ending'))
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

    def processGuess(self):
        
        playScreen = self.navigation_bar.get_screen('play')
        if (playScreen.rounds < playScreen.maxRounds):
            try:
                guessHeight = int(playScreen.ids.altitude.text)
                guessProm = int(playScreen.ids.prominence.text)
                guessIso = int(playScreen.ids.isolation.text)
                
                actualHeight = int(playScreen.mountain.altitude)
                actualProm = int(playScreen.mountain.prominence)
                actualIso = int(playScreen.mountain.isolation)
                # Update values
                playScreen.score += int(score.score(guessHeight, guessProm, guessIso, actualHeight, actualProm, actualIso))
                playScreen.rounds += 1
                playScreen.maxScore += 10
                playScreen.mountain = game_logic.RandomMountain()
                # Reset fields
                playScreen.ids.altitude.text = ""
                playScreen.ids.prominence.text = ""
                playScreen.ids.isolation.text = ""
                playScreen.ids.valueError.text = ""
                # Update Screen tags
                playScreen.imageName = "images/" + str(playScreen.mountain.rank) + ".jpg"
                playScreen.mountainName = str(playScreen.mountain.name)
                playScreen.currentRound = "Round " + str(playScreen.rounds) + "/" + str(playScreen.maxRounds)
                playScreen.currentScore = str(playScreen.score) + "/" + str(playScreen.maxScore)
            except ValueError:
                playScreen.ids.valueError.text = "Please Enter a valid number"
        else:
            try:   
                guessHeight = int(playScreen.ids.altitude.text)
                guessProm = int(playScreen.ids.prominence.text)
                guessIso = int(playScreen.ids.isolation.text)
                actualHeight = int(playScreen.mountain.altitude)
                actualProm = int(playScreen.mountain.prominence)
                actualIso = int(playScreen.mountain.isolation)
                playScreen.score += int(score.score(guessHeight, guessProm, guessIso, actualHeight, actualProm, actualIso))
                playScreen.maxScore += 10
                self.set_screen('ending')
                self.navigation_bar.get_screen('ending').ids.finalScore.text = "[b]"+str(playScreen.score) + "/" + str(playScreen.maxScore)+"[/b]"
            except ValueError:
                playScreen.ids.valueError.text = "Please Enter a valid number"

    def resetGame(self):
        playScreen = self.navigation_bar.get_screen('play')
        playScreen.rounds = 1
        playScreen.maxRounds = 5
        playScreen.score = 0
        playScreen.maxScore = 0

        playScreen.mountain = game_logic.RandomMountain()
        playScreen.imageName = "images/" + str(playScreen.mountain.rank) + ".jpg"
        playScreen.mountainName = str(playScreen.mountain.name)
        playScreen.currentRound = "Round " + str(playScreen.rounds) + "/" + str(playScreen.maxRounds)
        playScreen.currentScore = str(playScreen.score) + "/" + str(playScreen.maxScore)

        self.set_screen('home')
            
    def test(self):
        print("hi")
    

if __name__ == '__main__':
    MountainApp().run()