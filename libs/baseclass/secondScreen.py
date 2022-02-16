from re import A
from kivymd.uix.screen import MDScreen
from kivy.properties import StringProperty

class SecondScreen(MDScreen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def toFirstScreen(self):
        self.parent.current = 'firstScreen'
        pass