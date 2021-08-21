from manim import *
import color

class MovingFrameBox(Scene):
    def construct(self):

        self.camera.background_color = color.BACKGROUND

        exp1=Text('2').scale(0.3).set_color(BLACK).move_to(RIGHT * 1 + DOWN * 2)
        exp2=Text('2').scale(0.3).set_color(BLACK).move_to(LEFT * 1 + DOWN * 2)
        self.play(Write(exp1), Write(exp2))