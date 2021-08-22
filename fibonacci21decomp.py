from PIL.Image import FASTOCTREE
from manim import *
from functions import *
import color

def moveEquation(equations,loop,baseText,t1,t2,t3,t4,self):
    equations[loop].add(baseText.copy(), t1[loop].copy(), t2[7-loop].copy(), t3[loop].copy(), t4[7-loop].copy())
    self.play(equations[loop].animate.shift(LEFT * 6 + UP * (4.75 - loop * 0.5)))
    return loop + 1

class DecompDot(Scene):

    def construct(self):
        loop = 0
        fibo = [0,1,1,2,3,5,8,13,21]

        self.camera.background_color = color.BACKGROUND
        dots = [Dot().set_color(color.RED).move_to(UP * 0.25 * (10-i) + RIGHT * 3) for i in range(0,21)]

        baseText = Text('×     +     ×').scale(0.5).set_color(BLACK).move_to(DOWN * 3 + RIGHT * 3)

        name = Text('Fibonacci Decomposition').set_color(BLACK).move_to(UP * 3)

        t1 = VGroup()
        t2 = VGroup()
        t3 = VGroup()
        t4 = VGroup()

        for n in range(0,8):
            t1.add(Text(str(fibo[8-n])).set_color(color.RED))
            t2.add(Text(str(fibo[8-n])).set_color(color.RED))
            t3.add(Text(str(fibo[8-n-1])).set_color(color.BLUE))
            t4.add(Text(str(fibo[8-n-1])).set_color(color.BLUE))

        t1.scale(0.5).arrange(DOWN).move_to(LEFT * (1.15 - 3) + DOWN * (1.75 + 3))
        t2.scale(0.5).arrange(DOWN).move_to(LEFT * (0.4 - 3) + UP * (1.75 - 3))
        t3.scale(0.5).arrange(DOWN).move_to(RIGHT * (0.4 + 3) + DOWN * (1.75 + 3))
        t4.scale(0.5).arrange(DOWN).move_to(RIGHT * (1.15 + 3) + UP * (1.75 - 3))
        self.add(t1, t2, t3, t4)

        numberhidebox1 = Square().scale(2).move_to(UP * (2.25 - 3) + RIGHT * 3.5)
        numberhidebox1.set_fill(color.BACKGROUND, opacity=1).set_color(color.BACKGROUND)
        numberhidebox2 = Square().scale(2).move_to(DOWN * 5.25 + RIGHT * 3.5)
        numberhidebox2.set_fill(color.BACKGROUND, opacity=1).set_color(color.BACKGROUND)
        self.add(numberhidebox1, numberhidebox2)

        decompView = Rectangle(color=color.YELLOW, width=3.5, height=4.5).move_to(LEFT * 3)
        equations = [VGroup() for i in range(0,8)]
        
        self.play(FadeIn(decompView), FadeIn(baseText), FadeIn(t1), FadeIn(t2), FadeIn(t3), FadeIn(t4), *[GrowFromCenter(dots[i]) for i in range(0,21)])

        self.wait(1)

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        group1 = VGroup()
        group1.add(*[dots[i] for i in range(0,8)])
        group2 = VGroup()
        group2.add(*[dots[i] for i in range(8,21)])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125), group2.animate.shift(LEFT * 0.125), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 13))

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        group1.remove(*[dots[i] for i in range(0,8)])
        group2.add(*[dots[i] for i in range(0,8)])
        group2.remove(*[dots[i] for i in range(8,13)])
        group1.add(*[dots[i] for i in range(8,13)])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 3), group2.animate.set_color(color.RED).shift(LEFT * 0.125), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 8))

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        group1.remove(*[dots[i] for i in range(8,13)])
        group2.add(*[dots[i] for i in range(8,13)])
        group2.remove(*[dots[i] for i in [0,1,2,13,14,15]])
        group1.add(*[dots[i] for i in [0,1,2,13,14,15]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 4), group2.animate.set_color(color.RED).shift(LEFT * 0.25), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 5))

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        group1.remove(*[dots[i] for i in [0,1,2,13,14,15]])
        group2.add(*[dots[i] for i in [0,1,2,13,14,15]])
        group2.remove(*[dots[i] for i in [16,17,3,4,8,9]])
        group1.add(*[dots[i] for i in [16,17,3,4,8,9]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 7), group2.animate.set_color(color.RED).shift(LEFT * 0.125 * 3), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 3))

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        group1.remove(*[dots[i] for i in [16,17,3,4,8,9]])
        group2.add(*[dots[i] for i in [16,17,3,4,8,9]])
        group2.remove(*[dots[i] for i in [18,5,10,0,13]])
        group1.add(*[dots[i] for i in [18,5,10,0,13]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 11), group2.animate.set_color(color.RED).shift(LEFT * 0.125 * 5), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 2))

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        group1.remove(*[dots[i] for i in [18,5,10,0,13]])
        group2.add(*[dots[i] for i in [18,5,10,0,13]])
        group2.remove(*[dots[i] for i in [19,6,11,1,14,16,3,8]])
        group1.add(*[dots[i] for i in [19,6,11,1,14,16,3,8]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 18), group2.animate.set_color(color.RED).shift(LEFT * 0.125 * 8), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25))

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        group1.remove(*[dots[i] for i in [19,6,11,1,14,16,3,8]])
        group2.add(*[dots[i] for i in [19,6,11,1,14,16,3,8]])

        self.play(group2.animate.set_color(color.RED), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        self.play(FadeIn(name))

        self.wait(3)

        self.play(FadeOut(baseText, t1[7], t2[0], t3[7], t4[0], *dots, name))
        self.play(*[equations[i].animate.shift(RIGHT * 3) for i in range(0,8)], decompView.animate.shift(RIGHT * 3))
        self.play(FadeOut(*[equations[i][0] for i in range(0,8)]))
        
class DecompDotLongEnd (Scene):

    def construct(self):
        loop = 0
        fibo = [0,1,1,2,3,5,8,13,21]

        self.camera.background_color = color.BACKGROUND
        dots = [Dot().set_color(color.RED).move_to(UP * 0.25 * (10-i) + RIGHT * 3) for i in range(0,21)]

        baseText = Text('×     +     ×').scale(0.5).set_color(BLACK).move_to(DOWN * 3 + RIGHT * 3)

        name = Text('Fibonacci Decomposition').set_color(BLACK).move_to(UP * 3)

        t1 = VGroup()
        t2 = VGroup()
        t3 = VGroup()
        t4 = VGroup()

        for n in range(0,8):
            t1.add(Text(str(fibo[8-n])).set_color(color.RED))
            t2.add(Text(str(fibo[8-n])).set_color(color.RED))
            t3.add(Text(str(fibo[8-n-1])).set_color(color.BLUE))
            t4.add(Text(str(fibo[8-n-1])).set_color(color.BLUE))

        t1.scale(0.5).arrange(DOWN).move_to(LEFT * (1.15 - 3) + DOWN * (1.75 + 3))
        t2.scale(0.5).arrange(DOWN).move_to(LEFT * (0.4 - 3) + UP * (1.75 - 3))
        t3.scale(0.5).arrange(DOWN).move_to(RIGHT * (0.4 + 3) + DOWN * (1.75 + 3))
        t4.scale(0.5).arrange(DOWN).move_to(RIGHT * (1.15 + 3) + UP * (1.75 - 3))
        self.add(t1, t2, t3, t4)

        numberhidebox1 = Square().scale(2).move_to(UP * (2.25 - 3) + RIGHT * 3.5)
        numberhidebox1.set_fill(color.BACKGROUND, opacity=1).set_color(color.BACKGROUND)
        numberhidebox2 = Square().scale(2).move_to(DOWN * 5.25 + RIGHT * 3.5)
        numberhidebox2.set_fill(color.BACKGROUND, opacity=1).set_color(color.BACKGROUND)
        self.add(numberhidebox1, numberhidebox2)

        decompView = Rectangle(color=color.YELLOW, width=3.5, height=4.5).move_to(LEFT * 3)
        equations = [VGroup() for i in range(0,8)]
        
        self.play(FadeIn(decompView), FadeIn(baseText), FadeIn(t1), FadeIn(t2), FadeIn(t3), FadeIn(t4), *[GrowFromCenter(dots[i]) for i in range(0,21)])

        self.wait(1)

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        group1 = VGroup()
        group1.add(*[dots[i] for i in range(0,8)])
        group2 = VGroup()
        group2.add(*[dots[i] for i in range(8,21)])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125), group2.animate.shift(LEFT * 0.125), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 13))

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        group1.remove(*[dots[i] for i in range(0,8)])
        group2.add(*[dots[i] for i in range(0,8)])
        group2.remove(*[dots[i] for i in range(8,13)])
        group1.add(*[dots[i] for i in range(8,13)])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 3), group2.animate.set_color(color.RED).shift(LEFT * 0.125), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 8))

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        group1.remove(*[dots[i] for i in range(8,13)])
        group2.add(*[dots[i] for i in range(8,13)])
        group2.remove(*[dots[i] for i in [0,1,2,13,14,15]])
        group1.add(*[dots[i] for i in [0,1,2,13,14,15]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 4), group2.animate.set_color(color.RED).shift(LEFT * 0.25), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 5))

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        group1.remove(*[dots[i] for i in [0,1,2,13,14,15]])
        group2.add(*[dots[i] for i in [0,1,2,13,14,15]])
        group2.remove(*[dots[i] for i in [16,17,3,4,8,9]])
        group1.add(*[dots[i] for i in [16,17,3,4,8,9]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 7), group2.animate.set_color(color.RED).shift(LEFT * 0.125 * 3), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 3))

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        group1.remove(*[dots[i] for i in [16,17,3,4,8,9]])
        group2.add(*[dots[i] for i in [16,17,3,4,8,9]])
        group2.remove(*[dots[i] for i in [18,5,10,0,13]])
        group1.add(*[dots[i] for i in [18,5,10,0,13]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 11), group2.animate.set_color(color.RED).shift(LEFT * 0.125 * 5), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 2))

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        group1.remove(*[dots[i] for i in [18,5,10,0,13]])
        group2.add(*[dots[i] for i in [18,5,10,0,13]])
        group2.remove(*[dots[i] for i in [19,6,11,1,14,16,3,8]])
        group1.add(*[dots[i] for i in [19,6,11,1,14,16,3,8]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 18), group2.animate.set_color(color.RED).shift(LEFT * 0.125 * 8), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25))

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        group1.remove(*[dots[i] for i in [19,6,11,1,14,16,3,8]])
        group2.add(*[dots[i] for i in [19,6,11,1,14,16,3,8]])

        self.play(group2.animate.set_color(color.RED), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))

        loop = moveEquation(equations,loop,baseText,t1,t2,t3,t4,self)

        self.play(FadeIn(name))

        self.wait(11)

        self.play(FadeIn(Square().scale(10).set_fill(color.BACKGROUND).set_opacity(1)))

class Decomp(Scene):

    def construct(self):

        fibo = fiboarray_extended(-18, 18)

        self.camera.background_color = color.BACKGROUND

        fibonacci = VGroup(*[Text(str(fibo[i])).set_color(BLACK) for i in range(0, 35)]).arrange(RIGHT * 4).move_to(UP * 2.5 + LEFT * 10)

        baseText = Text('×     +     ×           =   21').scale(0.5).set_color(BLACK).move_to(RIGHT * 1.075)
        decompView = Rectangle(color=color.YELLOW, width=3.5, height=4.5).move_to(ORIGIN)
        t1 = VGroup()
        t2 = VGroup()
        t3 = VGroup()
        t4 = VGroup()

        for n in range(0,35):
            t1.add(Text(str(fibo[-n + 7 + 1])).set_color(color.RED))
            t2.add(Text(str(fibo[n+1])).set_color(color.RED))
            t3.add(Text(str(fibo[-n + 7])).set_color(color.BLUE))
            t4.add(Text(str(fibo[n])).set_color(color.BLUE))

        t1.scale(0.5).arrange(DOWN).move_to(LEFT * (1.15))
        t2.scale(0.5).arrange(DOWN).move_to(LEFT * (0.4))
        t3.scale(0.5).arrange(DOWN).move_to(RIGHT * (0.4))
        t4.scale(0.5).arrange(DOWN).move_to(RIGHT * (1.15))

        numbers = VGroup(t1, t2, t3, t4)
        numbers.shift(UP * 2.25)

        numberhideboxes = VGroup(Square().scale(2).move_to(UP * (4)).set_fill(color.BACKGROUND, opacity=1).set_color(color.BACKGROUND), Square().scale(2).move_to(DOWN * 4).set_fill(color.BACKGROUND, opacity=1).set_color(color.BACKGROUND))

        self.add(numbers, numberhideboxes, decompView)
        self.wait(1.8)
        self.play(numbers.animate.shift(DOWN), decompView.animate.shift(DOWN), numberhideboxes.animate.shift(DOWN), FadeIn(fibonacci))
        self.wait(1)
        self.play(fibonacci.animate.shift(RIGHT * 14), run_time=5)
        self.wait(3)
        self.play(FadeOut(fibonacci), numbers.animate.shift(UP * 0.75), decompView.animate.shift(UP).stretch_to_fit_height(6), numberhideboxes[0].animate.shift(UP * 2), Write(baseText))
        self.wait(1)
        for i in range(0,7):
            self.play(numbers.animate.shift(UP * 0.5), run_time=0.75)
        self.wait(2)
        self.play(FadeIn(Square().scale(10).set_fill(color.BACKGROUND).set_opacity(1)))
