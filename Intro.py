from manim import *
from numpy.core.records import array
from functions import *
import color

class Title(Scene):

    def construct(self):
        self.camera.background_color = color.BACKGROUND
        title = Text('Fibonacci Magic').scale(1.5).set_color(color.BLUE)
        subtitle = Text('An exploration of mysterious methods').scale(0.7).set_color(color.RED)
        wholeTitle = VGroup(title, subtitle).arrange(DOWN)
        self.play(Write(title), FadeIn(subtitle), run_time=3)
        self.wait(3)
        self.play(FadeOut(wholeTitle))

class AboutFibo(Scene):

    def construct(self):
        self.camera.background_color = color.BACKGROUND
        fibo = fiboarray(9)

        dotGroups1 = VGroup()
        dotGroups2 = VGroup().add(Dot().set_color(color.RED).move_to(DOWN * 2 + RIGHT * 1.25 *(-3)))
        dotGroups2old = VGroup()
        text = VGroup()
        for i in range(0,9):
            text.add(Text(str(fibo[i])).move_to(DOWN * 2.75 + RIGHT * 1.25 * (-4+i)).set_color(BLACK).scale(0.8))

        self.play(FadeIn(text[0]))
        self.play(FadeIn(dotGroups2), FadeIn(text[1]))

        for i in range(2,9):
            dotGroups1 = dotGroups1.copy()
            dotGroups2old = dotGroups2
            dotGroups2 = dotGroups2old.copy()
            textcopy = VGroup(text[i-2].copy(), text[i-1].copy())
            self.play(dotGroups1.animate.shift(RIGHT * 2 * 1.25 + UP * 0.25 * fibo[i-1]).set_color(color.BLUE), dotGroups2.animate.shift(RIGHT * 1.25), Transform(textcopy, text[i]))
            dotGroups2.add(dotGroups1)
            dotGroups1 = dotGroups2old
            self.play(dotGroups2.animate.set_color(color.RED))
            
        self.wait(2)

        rect = Rectangle(color=color.YELLOW, width=2.25, height=1).move_to(DOWN * 2.75 + RIGHT * 0.625)

        self.play(FadeIn(rect))

        self.play(rect.animate.shift(LEFT * 2 * 1.25), run_time=1.75)

        self.play(rect.animate.shift(RIGHT * 3 * 1.25), run_time=2.5)

        self.play(rect.animate.shift(LEFT * 1 * 1.25), run_time=1.25)

        self.play(rect.animate.shift(RIGHT * 2 * 1.25), run_time=1.75)

        self.play(rect.animate.shift(LEFT * 3 * 1.25), run_time=2.25)

        self.wait(0.5)

        self.play(FadeIn(Square().scale(10).set_fill(color.BACKGROUND).set_opacity(1)))


