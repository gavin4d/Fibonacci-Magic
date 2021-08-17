from manim import *
from functions import *
import color

class RectangleExample(Scene):
    def construct(self):
        rect = Rectangle(color=BLUE, width=1.0, height=4.0)
        self.add(rect)

        m = 1
        fibo = fiboarray(10)
        last = len(fibo)  # keeps track of the length of the fibo array

        self.camera.background_color = color.BACKGROUND
        dots = [Dot().set_color(color.RED).move_to(UP * 0.25 * (24 - i)) for i in range(0, fibo[-1])]

        baseText = Text('×     +     ×').scale(0.5).set_color(BLACK).move_to(DOWN * 3)

        t1 = VGroup()
        t2 = VGroup()
        t3 = VGroup()
        t4 = VGroup()

        for n in range(1, last):
            t1.add(Text(str(fibo[last - n])).set_color(color.RED))
            t2.add(Text(str(fibo[last - n])).set_color(color.RED))
            t3.add(Text(str(fibo[last - n - m])).set_color(color.BLUE))
            t4.add(Text(str(fibo[last - n - m])).set_color(color.BLUE))

        t1.scale(0.5).arrange(DOWN).move_to(LEFT * 1.15 + DOWN * (2 + 3))
        t2.scale(0.5).arrange(DOWN).move_to(LEFT * 0.4 + UP * (2 - 3))
        t3.scale(0.5).arrange(DOWN).move_to(RIGHT * 0.4 + DOWN * (2 + 3))
        t4.scale(0.5).arrange(DOWN).move_to(RIGHT * 1.15 + UP * (2 - 3))

        rect = Rectangle(color=BLUE, width=0.5, height=1.0)
        # rect.move_to(RIGHT * 0.4 + DOWN * (2 + 3))

        self.add(t1, t2, t3, t4, rect)

        # numberhidebox1 = Square().scale(2).move_to(UP * (2.25 - 3))
        # numberhidebox1.set_fill(color.BACKGROUND, opacity=1)
        # numberhidebox2 = Square().scale(2).move_to(DOWN * 5.25)
        # numberhidebox2.set_fill(color.BACKGROUND, opacity=1)
        # self.add(numberhidebox1, numberhidebox2)

        self.play(FadeIn(rect), FadeIn(baseText),
                  FadeIn(t1), FadeIn(t2), FadeIn(t3), FadeIn(t4), GrowFromCenter(dots[0]),
                  GrowFromCenter(dots[1]), GrowFromCenter(dots[2]), GrowFromCenter(dots[3]),
                  GrowFromCenter(dots[4]), GrowFromCenter(dots[5]), GrowFromCenter(dots[6]),
                  GrowFromCenter(dots[7]), GrowFromCenter(dots[8]), GrowFromCenter(dots[9]),
                  GrowFromCenter(dots[10]), GrowFromCenter(dots[11]), GrowFromCenter(dots[12]),
                  GrowFromCenter(dots[13]), GrowFromCenter(dots[14]), GrowFromCenter(dots[15]),
                  GrowFromCenter(dots[16]), GrowFromCenter(dots[17]), GrowFromCenter(dots[18]),
                  GrowFromCenter(dots[19]), GrowFromCenter(dots[20]), GrowFromCenter(dots[21]),
                  GrowFromCenter(dots[22]), GrowFromCenter(dots[23]), GrowFromCenter(dots[24]),
                  GrowFromCenter(dots[25]), GrowFromCenter(dots[26]), GrowFromCenter(dots[27]),
                  GrowFromCenter(dots[28]), GrowFromCenter(dots[29]), GrowFromCenter(dots[30]),
                  GrowFromCenter(dots[31]), GrowFromCenter(dots[32]), GrowFromCenter(dots[33]))

