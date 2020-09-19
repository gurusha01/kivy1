from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse,Line
from random import random
from kivy.uix.button import Button

class Paint(Widget):
    def on_touch_down(self,touch): #on_touch_down is a specific function responds to touch
            color = (random(), random(), random())
            with self.canvas:
                Color(*color)
                d = 30.
                #Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
                touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]



class jazzy(App,Widget):
    def build(self):
        self.painter=Paint()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        self.add_widget(self.painter)
        self.add_widget(clearbtn)
        return self
        
    def clear_canvas(self, obj):
        self.painter.canvas.clear()

if __name__ == '__main__':
    jazzy().run()

        
