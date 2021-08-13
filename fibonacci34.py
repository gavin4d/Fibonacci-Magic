from manim import *
from functions import *

class Start(Scene):

    def construct(self):
        i=1
        fibo = fiboarray(10)
        last = len(fibo) #keeps track of the length of the fibo array
        self.camera.background_color = WHITE
        dots = [Dot().set_color(RED).move_to(UP * 0.25 * (10-i)) for i in range(0,fibo[-1])]

        baseText = Text('  ×   +   ×  ').scale(0.5).set_color(BLACK).move_to(DOWN * 3)

        t1 = VGroup()
        t2 = VGroup()
        t3 = VGroup()
        t4 = VGroup()

        for n in range(1,last):
            t1.add(Text(str(fibo[last - n])).set_color(RED))
            t2.add(Text(str(fibo[last - n])).set_color(RED))
            t3.add(Text(str(fibo[last - n - i])).set_color(BLUE))
            t4.add(Text(str(fibo[last - n - i])).set_color(BLUE))
