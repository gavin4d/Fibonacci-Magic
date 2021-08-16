from manim import *
from functions import *
import color

class AddingSquares(Scene):

    def construct(self):
        self.camera.background_color = color.BACKGROUND
        print('First fibonacci (F value):')
        n = int(input())
        fibo = fiboarray(2*n+2)


        dotGroup1 = VGroup()
        for i in range(0, pow(fibo[n],2)):
            dotGroup1.add(Dot().set_color(color.BLUE))
        dotGroup1.arrange_in_grid(rows=fibo[n], cols=fibo[n], buff=0.09).move_to(LEFT * 4 + DOWN * 0.25 * fibo[n-1]/2)

        dotGroup2 = VGroup()
        for i in range(0, pow(fibo[n+1],2)):
            dotGroup2.add(Dot().set_color(color.RED))
        dotGroup2.arrange_in_grid(rows=fibo[n+1], cols=fibo[n+1], buff=0.09)

        symbols = VGroup().add(Text('+').move_to(LEFT * (4 - (fibo[n] * 0.125) + fibo[n+1] * 0.125)/2).set_color(BLACK)).add(Text('=').move_to(RIGHT * (4 + fibo[n+1] * 0.125)/2).set_color(BLACK))

        labels = VGroup()
        labels.add(Text(str(fibo[n])).set_color(BLACK).move_to(LEFT * 4 + DOWN * 0.25 * (fibo[n+1]/2 + 4)))
        labels.add(Text(str(fibo[n+1])).set_color(BLACK).move_to(DOWN * 0.25 * (fibo[n+1]/2 + 4)))
        labels.add(Tex('$f_' + str(n) + '$').set_color(BLACK).move_to(LEFT * 4 + DOWN * 0.25 * (fibo[n+1]/2 + 8)))
        labels.add(Tex('$f_' + str(n+1) + '$').set_color(BLACK).move_to(DOWN * 0.25 * (fibo[n+1]/2 + 8)))

        self.play(FadeIn(labels,dotGroup1,dotGroup2,symbols[0]))
        self.wait(1.5)

        dotGroup1Copy = dotGroup1.copy()
        dotGroup2Copy = dotGroup2.copy()

        labels.add(Text(str(fibo[2*n+1])).set_color(BLACK).move_to(RIGHT * 6 + UP * 0.5))
        labels.add(Tex('$f_' + str(2*n + 1) + '$').set_color(BLACK).move_to(RIGHT * 6 + DOWN * 0.5))
        brace = BraceBetweenPoints(RIGHT * 5 + UP * 0.25 * fibo[2*n+1]/2, RIGHT * 5 + DOWN * 0.25 * fibo[2*n+1]/2).set_color(BLACK).rotate(PI)

        self.play(FadeIn(symbols[1], labels[4], labels[5], brace), dotGroup1Copy.animate.arrange(DOWN * 0.375).move_to(RIGHT * 4 + UP * 0.1274 * (fibo[2*n+1] - pow(fibo[n], 2))), dotGroup2Copy.animate.arrange(DOWN * 0.375).move_to(RIGHT * 4 + DOWN * 0.1274 * (fibo[2*n+1] - pow(fibo[n+1], 2))))
        self.wait(2)
        self.play(FadeIn(Square().scale(10).set_fill(color.BACKGROUND).set_opacity(1)))