from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty

class FirstScreen(MDScreen):
    def toSecondScreen(self):
        self.parent.current = 'secondScreen'