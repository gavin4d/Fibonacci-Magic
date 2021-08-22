from manim import *

import color
from functions import *


class PauseOnSquare(MovingCameraScene):

    def construct(self):
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
        self.add(t1, t2, t3, t4)

        numberhidebox1 = Square().scale(2).move_to(UP * (2.25 - 3))
        numberhidebox1.set_fill(color.BACKGROUND, opacity=1)
        numberhidebox2 = Square().scale(2).move_to(DOWN * 5.25)
        numberhidebox2.set_fill(color.BACKGROUND, opacity=1)
        self.add(numberhidebox1, numberhidebox2)

        self.camera.frame.save_state()
        camScale = 1.3

        self.play(self.camera.frame.animate.scale(camScale).move_to(UP * 1.5), FadeIn(baseText), FadeIn(t1), FadeIn(t2), FadeIn(t3), FadeIn(t4), *[GrowFromCenter(dots[i]) for i in range(0,34)])

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

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 3), group2.animate.set_color(color.RED).shift(LEFT * 0.125),
                  t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5),
                  t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 13))
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
        self.wait(1)

        newbaseText = Text('+').scale(0.5).set_color(BLACK).move_to(DOWN * 3)
        self.add(newbaseText)
        self.play(FadeOut(baseText), t1.animate.shift(RIGHT * 0.38), t2.animate.shift(LEFT * 0.38),
                  t3.animate.shift(RIGHT * 0.38), t4.animate.shift(LEFT * 0.38) )
        self.remove(t1, t3)
        exp1 = Text('2').scale(0.3).set_color(BLACK).move_to(RIGHT * 0.95 + DOWN * 2.75)
        exp2 = Text('2').scale(0.3).set_color(BLACK).move_to(LEFT * 0.6 + DOWN * 2.75)
        self.play(Write(exp1), Write(exp2))

        result = Text('= 34').scale(0.5).set_color(BLACK).move_to(RIGHT * 2 + DOWN * 3)
        self.play(Write(result))
        self.wait(1)

        thirtyfour = Text(str(fiboarray(10)[9])).scale(0.5).set_color(BLACK).move_to(LEFT * 0.375 + DOWN * 3)

        self.play(Transform(result, thirtyfour), FadeOut(exp1, exp2, newbaseText, t2[4], t4[4]))

        vgap = 0.55

        evenfibos = VGroup(Text("8"), Text("21"), Text("55"), Text("144"))
        oddfibos = VGroup(Text("5"), Text("13"), Text("34"), Text("89"))
        evenfibos.set_color(color.YELLOW).scale(0.5)
        oddfibos.set_color(BLACK).scale(0.5)


        redsize = 8
        bluesize = 5
        redgroup1 = VGroup()
        for i in range(redsize):
            for j in range(redsize):
                redgroup1.add(Dot([i * 0.25, j * 0.25, 0], color=color.RED))
        for i in range(bluesize):
            for j in range(bluesize):
                redgroup1.add(Dot([i * 0.25 + (redsize * 0.25), j * 0.25 + (redsize * 0.25), 0], color=color.BLUE))

        redgroup1.next_to(group1, RIGHT, buff= 1)
        redgroup1center = VGroup(redgroup1[24], redgroup1[32])
        oddfibos[3].next_to(redgroup1center, DOWN, buff=vgap)

        redsize = 3
        bluesize = 2
        redgroup2 = VGroup()
        for i in range(redsize):
            for j in range(redsize):
                redgroup2.add(Dot([i * 0.25, j * 0.25, 0], color=color.RED))
        for i in range(bluesize):
            for j in range(bluesize):
                redgroup2.add(Dot([i * 0.25 + (redsize * 0.25), j * 0.25 + (redsize * 0.25), 0], color=color.BLUE))

        redgroup2.next_to((group2), LEFT, buff=1)
        oddfibos[1].next_to(redgroup2[3], DOWN, buff=vgap)


        redsize = 2
        bluesize = 1
        redgroup3 = VGroup()
        for i in range(redsize):
            for j in range(redsize):
                redgroup3.add(Dot([i * 0.25, j * 0.25, 0], color=color.RED))
        for i in range(bluesize):
            for j in range(bluesize):
                redgroup3.add(Dot([i * 0.25 + (redsize * 0.25), j * 0.25 + (redsize * 0.25), 0], color=color.BLUE))


        redgroup3.next_to(redgroup2[1], LEFT, buff=1)
        redgroup3center = VGroup(redgroup3[0], redgroup3[2])
        oddfibos[0].next_to(redgroup3center, DOWN, buff=vgap)

        oddfibos[2].move_to(result)

        evenfibos[0].next_to(oddfibos[0], RIGHT, buff=0.65)
        evenfibos[1].next_to(oddfibos[1], RIGHT, buff=0.8)
        evenfibos[2].next_to(result, RIGHT, buff=1.2)
        evenfibos[3].next_to(oddfibos[3], RIGHT, buff=1.5)

        self.play(*[GrowFromCenter(redgroup3[i]) for i in range(0,5)], *[GrowFromCenter(redgroup2[i]) for i in range(0,13)], *[GrowFromCenter(redgroup1[i]) for i in range(0,89)], FadeIn(oddfibos))
        self.remove(oddfibos[2])

        self.wait(1)
        self.play(FadeIn(evenfibos))
        self.wait(2)

        labels = VGroup(Tex('$f_5$'), Tex('$f_7$'), Tex('$f_9$'), Tex('$f_{11}$'))
        labels.set_color(BLACK).scale(0.8)
        for i in range(4):
            labels[i].move_to(oddfibos[i].get_center())
        self.play(Transform(oddfibos[0], labels[0]), Transform(oddfibos[1], labels[1]), Transform(result,
        labels[2]), Transform(oddfibos[3], labels[3]), FadeOut(evenfibos))

        self.wait(3)
        self.play(FadeIn(Square().scale(10).set_fill(color.BACKGROUND).set_opacity(1)))