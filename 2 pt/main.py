from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window

class PaintApp(App):
    def build(self):
        self.window = FloatLayout()
        
        self.menu = BoxLayout(orientation="horizontal", pos=(0, 0))
        self.window.add_widget(self.menu)
        
        self.canvas = Widget(size_hint=(None, None), size=(100, 100), pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.window.add_widget(self.canvas)
        
        return self.window
        
if __name__ == "__main__":
    Window.clearcolor = (1, 1, 1, 1)
    PaintApp().run()
    