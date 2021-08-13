from manim import *
from functions import *

class Start(Scene):

    def construct(self):
        fibo=fiboarray(10)
        self.camera.background_color = WHITE
        dots = [Dot().set_color(RED).move_to(UP * 0.25 * (10-i)) for i in range(0,fibo[-1])]

        baseText = Text('  ×   +   ×  ').scale(0.5).set_color(BLACK).move_to(DOWN * 3)

        t1 = VGroup()
        t2 = VGroup()
        t3 = VGroup()
        t4 = VGroup()
