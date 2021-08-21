from manim import *
from functions import *
import color

class DecompDot(Scene):

    def construct(self):
        loop = 1
        fibo = [0,1,1,2,3,5,8,13,21]

        self.camera.background_color = color.BACKGROUND
        dots = [Dot().set_color(color.RED).move_to(UP * 0.25 * (10-i) + RIGHT * 3) for i in range(0,21)]

        fibonacci1 = VGroup().move_to(LEFT * 3 + UP).arrange(RIGHT)
        fibonacci2 = VGroup().move_to(LEFT * 3 + DOWN).arrange(RIGHT)

        braceLeft = BraceBetweenPoints(dots[0].get_top(), dots[20].get_bottom()).set_color(color.YELLOW)
        braceBottom = BraceBetweenPoints(dots[20].get_left(), dots[20].get_right()).set_color(color.YELLOW)
        Ltext = braceLeft.get_tex(str(fibo[-loop])).set_color(color.RED)
        Btext = braceBottom.get_tex(str(fibo[loop+1])).set_color(color.BLUE)
        loop += 1
        
        self.play( FadeIn(fibonacci1, fibonacci2, braceLeft, braceBottom, Ltext, Btext), *[GrowFromCenter(dots[i]) for i in range(0,21)])

        self.wait(1)

        group1 = VGroup()
        group1.add(*[dots[i] for i in range(0,8)])
        group2 = VGroup()
        group2.add(*[dots[i] for i in range(8,21)])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125), group2.animate.shift(LEFT * 0.125), braceBottom.animate.stretch_to_fit_width(3), FadeOut(braceLeft, braceBottom), Ltext.animate.move_to(LEFT * (6 - (loop-1)) + UP), Btext.animate.move_to(LEFT * (6 - (loop-1)) + DOWN))
        self.play(group1.animate.shift(DOWN * 0.25 * 13))

        braceLeft = BraceBetweenPoints(dots[8].get_top(), dots[20].get_bottom()).set_color(color.YELLOW)
        braceBottom = BraceBetweenPoints(dots[20].get_left(), dots[7].get_right()).set_color(color.YELLOW)
        Ltext = braceLeft.get_tex(str(fibo[-loop])).set_color(color.RED)
        Btext = braceBottom.get_tex(str(fibo[loop+1])).set_color(color.BLUE)
        loop += 1

        self.play(FadeIn(braceLeft, braceBottom, Ltext, Btext))

        group1.remove(*[dots[i] for i in range(0,8)])
        group2.add(*[dots[i] for i in range(0,8)])
        group2.remove(*[dots[i] for i in range(8,13)])
        group1.add(*[dots[i] for i in range(8,13)])
        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 3), group2.animate.set_color(color.RED).shift(LEFT * 0.125), FadeOut(braceLeft, braceBottom), Ltext.animate.move_to(LEFT * (6 - (loop-1)) + UP), Btext.animate.move_to(LEFT * (6 - (loop-1)) + DOWN))
        self.play(group1.animate.shift(DOWN * 0.25 * 8))

        braceLeft = BraceBetweenPoints(dots[13].get_top(), dots[20].get_bottom()).set_color(color.YELLOW)
        braceBottom = BraceBetweenPoints(dots[20].get_left(), dots[12].get_right()).set_color(color.YELLOW)
        Ltext = braceLeft.get_tex(str(fibo[-loop])).set_color(color.RED)
        Btext = braceBottom.get_tex(str(fibo[loop+1])).set_color(color.BLUE)
        loop += 1

        self.play(FadeIn(braceLeft, braceBottom, Ltext, Btext))

        group1.remove(*[dots[i] for i in range(8,13)])
        group2.add(*[dots[i] for i in range(8,13)])
        group2.remove(*[dots[i] for i in [0,1,2,13,14,15]])
        group1.add(*[dots[i] for i in [0,1,2,13,14,15]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 4), group2.animate.set_color(color.RED).shift(LEFT * 0.25), FadeOut(braceLeft, braceBottom), Ltext.animate.move_to(LEFT * (6 - (loop-1)) + UP), Btext.animate.move_to(LEFT * (6 - (loop-1)) + DOWN))
        self.play(group1.animate.shift(DOWN * 0.25 * 5))

        braceLeft = BraceBetweenPoints(dots[16].get_top(), dots[20].get_bottom()).set_color(color.YELLOW)
        braceBottom = BraceBetweenPoints(dots[20].get_left(), dots[2].get_right()).set_color(color.YELLOW)
        Ltext = braceLeft.get_tex(str(fibo[-loop])).set_color(color.RED)
        Btext = braceBottom.get_tex(str(fibo[loop+1])).set_color(color.BLUE)
        loop += 1

        self.play(FadeIn(braceLeft, braceBottom, Ltext, Btext))

        group1.remove(*[dots[i] for i in [0,1,2,13,14,15]])
        group2.add(*[dots[i] for i in [0,1,2,13,14,15]])
        group2.remove(*[dots[i] for i in [16,17,3,4,8,9]])
        group1.add(*[dots[i] for i in [16,17,3,4,8,9]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 7), group2.animate.set_color(color.RED).shift(LEFT * 0.125 * 3), FadeOut(braceLeft, braceBottom), Ltext.animate.move_to(LEFT * (6 - (loop-1)) + UP), Btext.animate.move_to(LEFT * (6 - (loop-1)) + DOWN))
        self.play(group1.animate.shift(DOWN * 0.25 * 3))

        braceLeft = BraceBetweenPoints(dots[18].get_top(), dots[20].get_bottom()).set_color(color.YELLOW)
        braceBottom = BraceBetweenPoints(dots[20].get_left(), dots[9].get_right()).set_color(color.YELLOW)
        Ltext = braceLeft.get_tex(str(fibo[-loop])).set_color(color.RED)
        Btext = braceBottom.get_tex(str(fibo[loop+1])).set_color(color.BLUE)
        loop += 1

        self.play(FadeIn(braceLeft, braceBottom, Ltext, Btext))

        group1.remove(*[dots[i] for i in [16,17,3,4,8,9]])
        group2.add(*[dots[i] for i in [16,17,3,4,8,9]])
        group2.remove(*[dots[i] for i in [18,5,10,0,13]])
        group1.add(*[dots[i] for i in [18,5,10,0,13]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 11), group2.animate.set_color(color.RED).shift(LEFT * 0.125 * 5), FadeOut(braceLeft, braceBottom), Ltext.animate.move_to(LEFT * (6 - (loop-1)) + UP), Btext.animate.move_to(LEFT * (6 - (loop-1)) + DOWN))
        self.play(group1.animate.shift(DOWN * 0.25 * 2))

        braceLeft = BraceBetweenPoints(dots[19].get_top(), dots[20].get_bottom()).set_color(color.YELLOW)
        braceBottom = BraceBetweenPoints(dots[20].get_left(), dots[0].get_right()).set_color(color.YELLOW)
        Ltext = braceLeft.get_tex(str(fibo[-loop])).set_color(color.RED)
        Btext = braceBottom.get_tex(str(fibo[loop+1])).set_color(color.BLUE)
        loop += 1

        self.play(FadeIn(braceLeft, braceBottom, Ltext, Btext))

        group1.remove(*[dots[i] for i in [18,5,10,0,13]])
        group2.add(*[dots[i] for i in [18,5,10,0,13]])
        group2.remove(*[dots[i] for i in [19,6,11,1,14,16,3,8]])
        group1.add(*[dots[i] for i in [19,6,11,1,14,16,3,8]])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 18), group2.animate.set_color(color.RED).shift(LEFT * 0.125 * 8), FadeOut(braceLeft, braceBottom), Ltext.animate.move_to(LEFT * (6 - (loop-1)) + UP), Btext.animate.move_to(LEFT * (6 - (loop-1)) + DOWN))
        self.play(group1.animate.shift(DOWN * 0.25))

        braceLeft = BraceBetweenPoints(dots[20].get_top(), dots[20].get_bottom()).set_color(color.YELLOW)
        braceBottom = BraceBetweenPoints(dots[20].get_left(), dots[8].get_right()).set_color(color.YELLOW)
        Ltext = braceLeft.get_tex(str(fibo[-loop])).set_color(color.RED)
        Btext = braceBottom.get_tex(str(fibo[loop+1])).set_color(color.BLUE)
        loop += 1

        self.play(FadeIn(braceLeft, braceBottom, Ltext, Btext))

        group1.remove(*[dots[i] for i in [19,6,11,1,14,16,3,8]])
        group2.add(*[dots[i] for i in [19,6,11,1,14,16,3,8]])

        self.play(group2.animate.set_color(color.RED), FadeOut(braceLeft, braceBottom), Ltext.animate.move_to(LEFT * (6 - (loop-1)) + UP), Btext.animate.move_to(LEFT * (6 - (loop-1)) + DOWN))

        self.wait(3)
        self.play(FadeIn(Square().scale(10).set_fill(color.BACKGROUND).set_opacity(1)))
