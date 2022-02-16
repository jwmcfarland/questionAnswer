import os
from os import environ
from pathlib import Path
from kivy.lang import Builder
from kivymd.app import MDApp

KV_DIR = f"{os.path.dirname(__file__)}/libs/kv"

os.environ["APP_ROOT"] = str(Path(__file__).parent)

for kv_file in os.listdir(KV_DIR):
    # Print kv filename each iteration. 
    # Can be useful for debugging
    #print(kv_file)
    with open(os.path.join(KV_DIR,kv_file),encoding="utf-8") as kv:
        builderString = Builder.load_string(kv.read())


KV = '''
#: import FirstScreen libs.baseclass.firstScreen.FirstScreen
#: import SecondScreen libs.baseclass.secondScreen.SecondScreen
ScreenManager:
    id: screen_manager
    FirstScreen
    SecondScreen
'''

class MyMDApp(MDApp):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title = "Starting App Title"
        self.toolbar = None

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        return Builder.load_string(KV)

if __name__=='__main__':
    m = MyMDApp()
    m.run()