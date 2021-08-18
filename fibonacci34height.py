from manim import *

import color
from functions import *


class Start(MovingCameraScene):

    def construct(self):
        m = 1
        fibo = fiboarray(10)
        last = len(fibo)  # keeps track of the length of the fibo array

        self.camera.background_color = color.BACKGROUND
        dots = [Dot().set_color(color.RED).move_to(UP * 0.25 * (24 - i)) for i in range(0, fibo[-1])]

        baseText = Text('×     +     ×').scale(0.5).set_color(BLACK).move_to(DOWN * 3)

        rect = Rectangle(color=color.YELLOW, width=0.43, height=0.4)
        rect.move_to(RIGHT * 0.4 + DOWN * 3)



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

        self.add(t1, t2, t3, t4)

        numberhidebox1 = Square().scale(2).move_to(UP * (2.25 - 3))
        numberhidebox1.set_fill(color.BACKGROUND, opacity=1)
        numberhidebox2 = Square().scale(2).move_to(DOWN * 5.25)
        numberhidebox2.set_fill(color.BACKGROUND, opacity=1)
        self.add(numberhidebox1, numberhidebox2)

        self.camera.frame.save_state()
        camScale = 1.3

        self.play(self.camera.frame.animate.scale(camScale).move_to(UP * 1.5), FadeIn(baseText), FadeIn(t1), FadeIn(t2), FadeIn(t3), FadeIn(t4), GrowFromCenter(dots[0]),
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

        group1 = VGroup()
        group1.add(*[dots[i] for i in range(0,13)])
        group2 = VGroup()
        group2.add(*[dots[i] for i in range(13,34)])


        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125), group2.animate.shift(LEFT * 0.125),
                  t1.animate.shift(UP * 0.5),t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5),
                  t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 21), Restore(self.camera.frame))
        self.wait(1)

        group1.remove(*[dots[i] for i in range(0,13)])
        group2.add(*[dots[i] for i in range(0,13)])
        group2.remove(*[dots[i] for i in range(13,21)])
        group1.add(*[dots[i] for i in range(13, 21)])

        brace = BraceBetweenPoints(dots[13].get_center(), dots[20].get_center(), color=color.YELLOW)
        self.add(brace)

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 3), group2.animate.set_color(color.RED).shift(LEFT * 0.125),
                  t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5),
                  t4.animate.shift(DOWN * 0.5))
        self.play(FadeIn(rect), FadeOut(brace), group1.animate.shift(DOWN * 0.25 * 13))
        self.wait(1)

        group1.remove(*[dots[i] for i in range(13, 21)])
        group2.add(*[dots[i] for i in range(13, 21)])
        group2.remove(*[dots[i] for i in [0, 1, 2, 3, 4, 21, 22, 23, 24, 25]])
        group1.add(*[dots[i] for i in [0, 1, 2, 3, 4, 21, 22, 23, 24, 25]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 4),
                  group2.animate.set_color(color.RED).shift(LEFT * 0.125 * 2),
                  t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5),
                  t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 8))
        self.wait(1)

        group1.remove(*[dots[i] for i in [0, 1, 2, 3, 4, 21, 22, 23, 24, 25]])
        group2.add(*[dots[i] for i in [0, 1, 2, 3, 4, 21, 22, 23, 24, 25]])
        group2.remove(*[dots[i] for i in [5, 6, 7, 26, 27, 28, 13, 14, 15]])
        group1.add(*[dots[i] for i in [5, 6, 7, 26, 27, 28, 13, 14, 15]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 7),
                  group2.animate.set_color(color.RED).shift(LEFT * 0.125 * 3),
                  t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5),
                  t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 5))
        self.wait(1)

        group1.remove(*[dots[i] for i in [5, 6, 7, 26, 27, 28, 13, 14, 15]])
        group2.add(*[dots[i] for i in [5, 6, 7, 26, 27, 28, 13, 14, 15]])
        group2.remove(*[dots[i] for i in [8, 9, 29, 30, 16, 17, 0, 1, 21, 22]])
        group1.add(*[dots[i] for i in [8, 9, 29, 30, 16, 17, 0, 1, 21, 22]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 11),
                  group2.animate.set_color(color.RED).shift(LEFT * 0.125 * 5),
                  t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5),
                  t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 3))
        self.wait(1)

        group1.remove(*[dots[i] for i in [8, 9, 29, 30, 16, 17, 0, 1, 21, 22]])
        group2.add(*[dots[i] for i in [8, 9, 29, 30, 16, 17, 0, 1, 21, 22]])
        group2.remove(*[dots[i] for i in [31, 10, 18, 23, 2, 26, 5, 13]])
        group1.add(*[dots[i] for i in [31, 10, 18, 23, 2, 26, 5, 13]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 18),
                  group2.animate.set_color(color.RED).shift(LEFT * 0.125 * 8),
                  t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5),
                  t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 2))
        self.wait(1)

        group1.remove(*[dots[i] for i in [31, 10, 18, 23, 2, 26, 5, 13]])
        group2.add(*[dots[i] for i in [31, 10, 18, 23, 2, 26, 5, 13]])
        group2.remove(*[dots[i] for i in [32, 19, 11, 24, 3, 27, 6, 14, 29, 8, 16, 21, 0]])
        group1.add(*[dots[i] for i in [32, 19, 11, 24, 3, 27, 6, 14, 29, 8, 16, 21, 0]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 29),
                  group2.animate.set_color(color.RED).shift(LEFT * 0.125 * 13),
                  t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5),
                  t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 1))
        self.wait(1)

        group1.remove(*[dots[i] for i in [32, 19, 11, 24, 3, 27, 6, 14, 29, 8, 16, 21, 0]])
        group2.add(*[dots[i] for i in [32, 19, 11, 24, 3, 27, 6, 14, 29, 8, 16, 21, 0]])

        self.play(group2.animate.set_color(color.RED), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5),
                  t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.wait(1)
        self.play(FadeIn(Square().scale(10).set_fill(color.BACKGROUND).set_opacity(1)))