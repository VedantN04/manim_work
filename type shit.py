from manim import*
class BraceAnnotation(Scene):
    def construct(self):
    dot = Dot([-2,-1,0])
    dot2 = Dot([2,1,0])
    line = Line(dot.get_center(), dot2.get_center()).set_color(BLUE_C)
    b1 = Brace(line)
    b1text = b1.get_text("Horizontal Distance")
    b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
    b2text = b2.get_text("x-x_1")

    self.add(line,dot, dot2, line, b1, b2, b1text, b2text)
