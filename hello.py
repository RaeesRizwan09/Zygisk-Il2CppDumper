from manim import *

class HelloScene(Scene):
    def construct(self):
        text = Text("Hello")
        self.play(Write(text))
        self.wait(2)
      
