from kivy.app import App
from kivy.uix.button import Button
from   kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import random

class FirstPage(Button):
    def __init__(self):
        super().__init__()
        self.text = "Hi"
        self.bind(on_press=self.switch)

    def switch(selfself, item):
        random_direction = random.choice(["left", "right", "up", "down"])
        myapp.screen_manager.transition = SlideTransition(direction=random_direction)
        myapp.screen_manager.current = "Second"



class SecondPage(Button):
    def __init__(self):
        super().__init__()
        self.text = "hi there"
        self.bind(on_press=self.switch)

    def switch(self, item):
        random_direction = random.choice(["left", "right", "up", "down"])
        myapp.screen_manager.transition = SlideTransition(direction=random_direction)
        myapp.screen_manager.current = "First"


class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.firstpage = FirstPage()
        screen = Screen(name="First")
        screen.add_widget(self.firstpage)
        self.screen_manager.add_widget(screen)

        self.secondpage = SecondPage()
        screen = Screen(name="Second")
        screen.add_widget(self.secondpage)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


myapp = MyApp()
myapp.run()