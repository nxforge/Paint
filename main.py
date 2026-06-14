from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Rectangle, Line
from random import random
from tkinter import filedialog, Tk
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.label import Label

class CanvasWidget(Widget):
    def __init__(self, **kwargs):
        super(CanvasWidget, self).__init__(**kwargs)
        self.linec = True
        self.ovalc = False
        self.squarec = False
        self.rad = 100
    
    
    def on_touch_down(self, touch):
        with self.canvas:
            if self.linec:
                Color(random(), random(), random(), 1)
                Ellipse(pos=(touch.x - self.rad // 2, touch.y - self.rad // 2), size=(self.rad, self.rad))
                self.line = Line(points=(touch.x, touch.y), width=self.rad // 2)
            if self.ovalc:
                Color(random(), random(), random(), 1)
                self.oval = Ellipse(pos=(touch.x, touch.y - self.rad), size=(self.rad, self.rad))
                self.oval_x = touch.x
                self.oval_y = touch.y
            if self.squarec:
                Color(random(), random(), random(), 1)
                self.square = Rectangle(pos=(touch.x, touch.y - self.rad), size=(self.rad, self.rad))
                self.square_x = touch.x
                self.square_y = touch.y


    def on_touch_move(self, touch):
        if self.linec:
            self.line.points += (touch.x, touch.y)
        if self.ovalc:
            self.oval.size = (touch.x - self.oval_x, touch.y - self.oval_y)
        if self.squarec:
            self.square.size = (touch.x - self.square_x, touch.y - self.square_y)
        
        
    def editing_shapes(self, shape):
        if shape == "oval":
            self.ovalc = True
        else:
            self.ovalc = False
        if shape == "square":
            self.squarec = True
        else:
            self.squarec = False
        if shape == "line":
            self.linec = True
        else:
            self.linec = False
            
            
    def editing_rad(self, value):
        self.rad = value
        

class PaintApp(App):
    def save(self, button):
        tk = Tk()
        tk.withdraw()
        file = filedialog.asksaveasfilename(title="save", initialfile=self.name_project.text, defaultextension="png")
        if file != "":
            self.canvas.export_to_png(file)


    def clear(self, button):
        self.canvas.canvas.clear()


    def fullscreen(self, button):
        if self.fullscreen_active:
            self.fullscreen_active = False
            Window.fullscreen = False
            self.fullscrreen_button.text = "Full screen"
        else:
            self.fullscreen_active = True
            Window.fullscreen = "auto"
            self.fullscrreen_button.text = "Window"



    def build(self):
        self.fullscreen_active = False
        self.icon = "icons\\icon_512x512.png"

        self.application = FloatLayout()

        self.canvas = CanvasWidget()
        self.application.add_widget(self.canvas)

        self.application.add_widget(Button(text="Save", pos=(0, 0), background_color=(0, 0, 0, 0.5), size_hint=(None, None), size=(100, 50), on_press=self.save))
        self.application.add_widget(Button(text="Clear", pos=(100, 0), background_color=(0, 0, 0, 0.5), size_hint=(None, None), size=(100, 50), on_press=self.clear))
        self.fullscrreen_button = Button(text="Full screen", pos=(200, 0), background_color=(0, 0, 0, 0.5), size_hint=(None, None), size=(100, 50), on_press=self.fullscreen)
        self.application.add_widget(self.fullscrreen_button)
        self.application.add_widget(Button(text="Oval", pos=(300, 0), background_color=(0, 0, 0, 0.5), size_hint=(None, None), size=(100, 50), on_press=lambda event: self.canvas.editing_shapes("oval")))
        self.application.add_widget(Button(text="Line", pos=(400, 0), background_color=(0, 0, 0, 0.5), size_hint=(None, None), size=(100, 50), on_press=lambda event: self.canvas.editing_shapes("line")))
        self.application.add_widget(Button(text="Square", pos=(500, 0), background_color=(0, 0, 0, 0.5), size_hint=(None, None), size=(100, 50), on_press=lambda event: self.canvas.editing_shapes("square")))
        self.name_project = TextInput(text="image", multiline=False, size_hint=(None, 0.04), size=(450, 0), pos_hint={"center_x": 0.5, "center_y": 0.98})
        self.application.add_widget(self.name_project)
        self.slider = Slider(value=100, max=500, min=1, pos=(50, 50), orientation="vertical", size_hint=(None, None), size=(100, 400))
        self.slider.on_touch_move = lambda event: self.canvas.editing_rad(self.slider.value)
        self.application.add_widget(self.slider)

        return self.application

if __name__ == "__main__":
    PaintApp().run()
