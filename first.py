from manim import *

class MyFirstScene(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        text = Text("Hello World!")

        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.play(Write(text))
        self.wait(1)