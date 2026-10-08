from manim import *
import numpy as np

class waves(Scene):
    def construct(self):
        a = Axes(x_range=[-50,50], y_range=[-8,8])

        graph = a.plot(lambda x: np.sin(x) + np.sin(x*0.737) + np.cos(x/2) + np.sin(x/0.60) + np.sin(x/1.2) + np.sin(x/0.335) + np.sin(x/0.913) + np.sin(x/1.3911) +np.sin(x/0.81) + np.sin(x/0.9), color=WHITE)

        s1 = a.plot(lambda x: np.sin(x))
        s2 = a.plot(lambda x: np. sin(x*0.737))
        s3 = a.plot(lambda x: np. cos(x/2))
        s4 = a.plot(lambda x: np. sin(x/0.69))
        s5 = a.plot(lambda x: np. sin(x/1.2))
        s6 = a.plot(lambda x: np. sin(x/0.335))
        s7 = a.plot(lambda x: np. sin(x/0.913))
        s8 = a.plot(lambda x: np. sin(x/1.3911))
        s9 = a.plot(lambda x: np.sin(x/0.81))
        s10 = a.plot(lambda x: np.sin(x/0.9))
    
        g = VGroup(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10)
        self.add(g)
        self.add(graph) 
        self.play(ReplacementTransform(graph, g))
        self.wait(3)

        