import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import random

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 1000))

class Ajeeth(App):
    def build(self):
        return MyRoot()

Ajeeth_S = Ajeeth()
Ajeeth_S.run()
