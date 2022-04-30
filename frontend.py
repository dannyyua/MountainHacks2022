from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar

class MountainApp(MDApp):
    def build(self):
        screen = MDScreen()
        #UI Widgets go here
        self.toolbar = MDToolbar(title = "Mountain Guesser")
        self.toolbar.pos_hint = {"top": 1}
        #Add Widget
        screen.add_widget(self.toolbar)
        
        return screen

if __name__ == '__main__':
    MountainApp().run()