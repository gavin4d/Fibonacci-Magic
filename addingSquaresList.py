from typing_extensions import runtime
from manim import *
from functions import *
import color

class AddingSquares(Scene):

    def construct(self):
        self.camera.background_color = color.BACKGROUND
        n = 1
        rows = 5
        fibo = fiboarray(2*(rows+n)+1)

        labels = [VGroup() for i in range(0,rows)]
        for i in range(0,rows):
            labels[i].add(Tex('$' + str(fibo[i+n]) + '$', '$^2\quad +\quad $', '$' + str(fibo[i+n+1]) + '$', '$^2\quad =\quad $', '$' + str(fibo[2*(i+n)+1]) + '$').set_color(BLACK).move_to(UP * 1.4 * (((rows-1)/2)-i)))
            for l in [0,2,4]:
                labels[i][0][l].set_color(color.BLUE)

            labels[i].add(Tex(fibo[2*(i+n)]).set_color(color.YELLOW).move_to(RIGHT * 1.92 + UP * 1.4 * (((rows-1)/2) - i + 0.5)))

            labels[i].add(Tex('$f$','$_{' + str(i+n) + '}$').set_color(BLACK).scale(0.8).move_to(LEFT * 1.85 + UP * 1.4 * (((rows-1)/2) - i - 0.35)))
            labels[i].add(Tex('$f$','$_{' + str(i+n+1) + '}$').set_color(BLACK).scale(0.8).move_to(UP * 1.4 * (((rows-1)/2) - i - 0.35)))
            labels[i].add(Tex('$f$','$_{' + str(2*(i+n)+1) + '}$').set_color(BLACK).scale(0.8).move_to(RIGHT * 1.95 + UP * 1.4 * (((rows-1)/2) - i - 0.35)))

            for l in range(2,5):
                labels[i][l][1].set_color(color.RED)

            if fibo[2*(i+n)+1] >= 10:
                labels[i][0].shift(RIGHT * .12)
                labels[i][4].shift(RIGHT * .12)

            if fibo[2*(i+n)] >= 10:
                labels[i][1].shift(RIGHT * .12)

        general = Tex('${f_n}^2\quad +\quad {f_{n+1}}^2\quad =\quad f_{2n+1}$').set_color(BLACK)

        self.play(LaggedStart(*[FadeIn(labels[i][0]) for i in range(0,rows)], lag_ratio=0.15, run_time=2))
        self.wait(4)
        self.play(LaggedStart(*[FadeIn(labels[i][1]) for i in range(0,rows)], lag_ratio=0.15, run_time=1))
        self.wait(6)
        self.play(FadeOut(*[labels[i][1] for i in range(0,rows)]))
        self.wait(0.5)
        self.play(LaggedStart(*[FadeIn(*[labels[i][l] for i in range(0,rows)]) for l in range(2,5)]))
        self.wait(8)
        self.play(FadeOut(*[labels[i][l] for i in range(0,rows) for l in [0,2,3,4]]))
        self.play(FadeIn(general))
        self.wait(5)
        self.play(FadeIn(Square().scale(10).set_fill(color.BACKGROUND).set_opacity(1)))