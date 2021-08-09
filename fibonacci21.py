from manim import *

class Start(Scene):

    def construct(self):
        i = 1
        fibo = [0,1,1,2,3,5,8,13,21]
        self.camera.background_color = WHITE
        dots = [Dot().set_color(RED).move_to(UP * 0.25 * (10-i)) for i in range(0,21)]

        baseText = Text('  ×   +   ×  ').scale(0.5).set_color(BLACK).move_to(DOWN * 3)

        t1 = VGroup()
        t2 = VGroup()
        t3 = VGroup()
        t4 = VGroup()


        for n in range(1,9):
            t1.add(Text(str(fibo[9-n])).set_color(RED))
            t2.add(Text(str(fibo[9-n])).set_color(RED))
            t3.add(Text(str(fibo[9-n-i])).set_color(BLUE))
            t4.add(Text(str(fibo[9-n-i])).set_color(BLUE))

        t1.scale(0.5).arrange(DOWN).move_to(LEFT * 0.9 + DOWN * (1.75 + 3))
        t2.scale(0.5).arrange(DOWN).move_to(LEFT * 0.3 + UP * (1.75 - 3))
        t3.scale(0.5).arrange(DOWN).move_to(RIGHT * 0.3 + DOWN * (1.75 + 3))
        t4.scale(0.5).arrange(DOWN).move_to(RIGHT * 0.9 + UP * (1.75 - 3))
        self.add(t1, t2, t3, t4)

        numberhidebox1 = Square().scale(2).move_to(UP * (2.25 - 3))
        numberhidebox1.set_fill(WHITE, opacity=1)
        numberhidebox2 = Square().scale(2).move_to(DOWN * 5.25)
        numberhidebox2.set_fill(WHITE, opacity=1)
        self.add(numberhidebox1, numberhidebox2)
        
        self.play(FadeIn(baseText), FadeIn(t1), FadeIn(t2), FadeIn(t3), FadeIn(t4), GrowFromCenter(dots[0]), GrowFromCenter(dots[1]), GrowFromCenter(dots[2]), GrowFromCenter(dots[3]), GrowFromCenter(dots[4]), GrowFromCenter(dots[5]), GrowFromCenter(dots[6]), GrowFromCenter(dots[7]), GrowFromCenter(dots[8]), GrowFromCenter(dots[9]), GrowFromCenter(dots[10]), GrowFromCenter(dots[11]), GrowFromCenter(dots[12]), GrowFromCenter(dots[13]), GrowFromCenter(dots[14]), GrowFromCenter(dots[15]), GrowFromCenter(dots[16]), GrowFromCenter(dots[17]), GrowFromCenter(dots[18]), GrowFromCenter(dots[19]), GrowFromCenter(dots[20]))

        group1 = VGroup()
        group1.add(*[dots[i] for i in range(0,8)])
        group2 = VGroup()
        group2.add(*[dots[i] for i in range(8,21)])

        self.play(group1.animate.set_color(BLUE).shift(RIGHT * 0.125), group2.animate.shift(LEFT * 0.125), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 13))
        self.wait(1)

        group1.remove(*[dots[i] for i in range(0,8)])
        group2.add(*[dots[i] for i in range(0,8)])
        group2.remove(*[dots[i] for i in range(8,13)])
        group1.add(*[dots[i] for i in range(8,13)])

        self.play(group1.animate.set_color(BLUE).shift(RIGHT * 0.125 * 3), group2.animate.set_color(RED).shift(LEFT * 0.125), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 8))
        self.wait(1)

        group1.remove(*[dots[i] for i in range(8,13)])
        group2.add(*[dots[i] for i in range(8,13)])
        group2.remove(*[dots[i] for i in [0,1,2,13,14,15]])
        group1.add(*[dots[i] for i in [0,1,2,13,14,15]])

        self.play(group1.animate.set_color(BLUE).shift(RIGHT * 0.125 * 4), group2.animate.set_color(RED).shift(LEFT * 0.25), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 5))
        self.wait(1)

        group1.remove(*[dots[i] for i in [0,1,2,13,14,15]])
        group2.add(*[dots[i] for i in [0,1,2,13,14,15]])
        group2.remove(*[dots[i] for i in [16,17,3,4,8,9]])
        group1.add(*[dots[i] for i in [16,17,3,4,8,9]])

        self.play(group1.animate.set_color(BLUE).shift(RIGHT * 0.125 * 7), group2.animate.set_color(RED).shift(LEFT * 0.125 * 3), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 3))
        self.wait(1)

        group1.remove(*[dots[i] for i in [16,17,3,4,8,9]])
        group2.add(*[dots[i] for i in [16,17,3,4,8,9]])
        group2.remove(*[dots[i] for i in [18,5,10,0,13]])
        group1.add(*[dots[i] for i in [18,5,10,0,13]])

        self.play(group1.animate.set_color(BLUE).shift(RIGHT * 0.125 * 11), group2.animate.set_color(RED).shift(LEFT * 0.125 * 5), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 2))
        self.wait(1)

        group1.remove(*[dots[i] for i in [18,5,10,0,13]])
        group2.add(*[dots[i] for i in [18,5,10,0,13]])
        group2.remove(*[dots[i] for i in [19,6,11,1,14,16,3,8]])
        group1.add(*[dots[i] for i in [19,6,11,1,14,16,3,8]])

        self.play(group1.animate.set_color(BLUE).shift(RIGHT * 0.125 * 18), group2.animate.set_color(RED).shift(LEFT * 0.125 * 8), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25))
        self.wait(1)

        group1.remove(*[dots[i] for i in [19,6,11,1,14,16,3,8]])
        group2.add(*[dots[i] for i in [19,6,11,1,14,16,3,8]])

        self.play(group2.animate.set_color(RED), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.wait(1)

