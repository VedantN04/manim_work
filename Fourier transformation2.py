from manim import *
import numpy as np

def fun_color(x):
    colors = [RED, ORANGE, GREEN, TEAL, BLUE, MAROON, YELLOW, PURPLE, LIGHT_PINK, BLUE_C]
    for i in range(len(x)):
        x[i].set_color(colors[i])
    return(x)


class waves(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(zoom = 0.6, phi = -0.5, theta = -90*DEGREES)

        a = ThreeDAxes(x_range=[-20, 20], y_range=[-8, 8])

        x_lab = a.get_x_axis_label("X axis")
        y_lab = a.get_y_axis_label("Y axis")
        Z_lab = a.get_z_axis_label("Z axis")




        graph = a.plot(
            lambda x: np.sin(x)
            + np.sin(x * 0.737)
            + np.cos(x / 2)
            + np.sin(x / 0.69)
            + np.sin(x / 1.2)
            + np.sin(x / 0.335)
            + np.sin(x / 0.913)
            + np.sin(x / 1.3911)
            + np.sin(x / 0.81)
            + np.sin(x / 0.9),
            color=WHITE,
        )

        s1 = a.plot(lambda x: np.sin(x) * 1.4)
        s2 = a.plot(lambda x: np.sin(x * 0.737) * 2)
        s3 = a.plot(lambda x: np.cos(x / 2) * 0.5)
        s4 = a.plot(lambda x: np.sin(x / 0.69) * 3)
        s5 = a.plot(lambda x: np.sin(x / 1.2) * 1.2)
        s6 = a.plot(lambda x: np.sin(x / 0.335) * 2.74)
        s7 = a.plot(lambda x: np.sin(x / 0.913) * 3.32)
        s8 = a.plot(lambda x: np.sin(x / 1.3911))
        s9 = a.plot(lambda x: np.sin(x / 0.81) * 2.3)
        s10 = a.plot(lambda x: np.sin(x / 0.9) * 1.6)

        g = VGroup(s1, s2, s3, s4, s5, s6, s7, s8, s9, s10)

        fun_color(g)

        self.add(graph)

        self.play(ReplacementTransform(graph, g))

        self.wait(3)