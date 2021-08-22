from manim import *
import color

class Credits(MovingCameraScene):

    def construct(self):
        i = 1
        fibo = [0,1,1,2,3,5,8,13,21]

        self.camera.background_color = color.BACKGROUND
        dots = [Dot().set_color(color.RED).move_to(UP * 0.25 * (10-i)) for i in range(0,21)]

        baseText = Text('  ×   +   ×  ').scale(0.5).set_color(BLACK).move_to(DOWN * 3)

        t1 = VGroup()
        t2 = VGroup()
        t3 = VGroup()
        t4 = VGroup()

        for n in range(1,9):
            t1.add(Text(str(fibo[9-n])).set_color(color.RED))
            t2.add(Text(str(fibo[9-n])).set_color(color.RED))
            t3.add(Text(str(fibo[9-n-i])).set_color(color.BLUE))
            t4.add(Text(str(fibo[9-n-i])).set_color(color.BLUE))

        t1.scale(0.5).arrange(DOWN).move_to(LEFT * 0.9 + DOWN * (1.75 + 3))
        t2.scale(0.5).arrange(DOWN).move_to(LEFT * 0.3 + UP * (1.75 - 3))
        t3.scale(0.5).arrange(DOWN).move_to(RIGHT * 0.3 + DOWN * (1.75 + 3))
        t4.scale(0.5).arrange(DOWN).move_to(RIGHT * 0.9 + UP * (1.75 - 3))
        self.add(t1, t2, t3, t4)

        numberhidebox1 = Square().scale(2).move_to(UP * (2.25 - 3))
        numberhidebox1.set_fill(color.BACKGROUND, opacity=1).set_color(color.BACKGROUND)
        numberhidebox2 = Square().scale(2).move_to(DOWN * 5.25)
        numberhidebox2.set_fill(color.BACKGROUND, opacity=1).set_color(color.BACKGROUND)

        creditsbox = Rectangle(color=BLACK, fill_opacity= 1, width= 5, height=7.5)
        creditsbox.shift(RIGHT * 6)
        lineSpace = 3.75

        creditstext = [VGroup(
          Text("Thanks for watching!")).arrange(DOWN * lineSpace), 
          VGroup(
          Text("A big thank you to"),
          Text("Grant Sanderson"),
          Text("of 3Blue1Brown"),
          Text("for inspiring us"),
          Text("to make"),
          Text("this video")).arrange(DOWN * lineSpace), 
          VGroup(
          Text("Phi Guys are an"),
          Text("entirely"),
          Text("original creation,"),
          Text("and not to be"),
          Text("confused with"),
          Text("Pi Guys")).arrange(DOWN * lineSpace), 
          VGroup(
          Text("No Phi Guys"),
          Text("or Pi Guys"),
          Text("were harmed"),
          Text("in the creation"),
          Text("of this video")).arrange(DOWN * lineSpace), 
          VGroup(
          Text("Animations created"),
          Text("with Manim."),
          Text("Thanks to everyone"),
          Text("in the"),
          Text("Manim community for"),
          Text("making such a"),
          Text("great math animation"),
          Text("library")).arrange(DOWN * lineSpace), 
          VGroup(
          Text("Music:\n"
               "\"Dolphin-esque\"\n"
               "    by Godmode.\n"
               "\"Wind Riders\"\n"
               "    by Asher Fulero.\n"
               "\"Sunrise in Paris\"\n"
               "    by Dan Henig.", line_spacing=lineSpace-1.5),).arrange(DOWN * lineSpace), 
          VGroup(
          Text("Don't forget to"),
          Text("like and subscribe")).arrange(DOWN * lineSpace), 
          VGroup(
          Text("Stay tuned"),
          Text("for future videos!")).arrange(DOWN * lineSpace)]

        for i in creditstext:
             i.scale(0.5).move_to(creditsbox)

        alldots = VGroup()
        alldots.add(*[dots[i] for i in range(0,21)])

        self.add(numberhidebox1, numberhidebox2, creditsbox)

        self.camera.frame.move_to(RIGHT * 3)

        self.play(Write(creditstext[0]), FadeIn(baseText), FadeIn(t1), FadeIn(t2), FadeIn(t3), FadeIn(t4), GrowFromCenter(dots[0]), GrowFromCenter(dots[1]), GrowFromCenter(dots[2]), GrowFromCenter(dots[3]), GrowFromCenter(dots[4]), GrowFromCenter(dots[5]), GrowFromCenter(dots[6]), GrowFromCenter(dots[7]), GrowFromCenter(dots[8]), GrowFromCenter(dots[9]), GrowFromCenter(dots[10]), GrowFromCenter(dots[11]), GrowFromCenter(dots[12]), GrowFromCenter(dots[13]), GrowFromCenter(dots[14]), GrowFromCenter(dots[15]), GrowFromCenter(dots[16]), GrowFromCenter(dots[17]), GrowFromCenter(dots[18]), GrowFromCenter(dots[19]), GrowFromCenter(dots[20]))

        group1 = VGroup()
        group1.add(*[dots[i] for i in range(0,8)])
        group2 = VGroup()
        group2.add(*[dots[i] for i in range(8,21)])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125), group2.animate.shift(LEFT * 0.125), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 13))
        self.play(FadeOut(creditstext[0]))

        group1.remove(*[dots[i] for i in range(0,8)])
        group2.add(*[dots[i] for i in range(0,8)])
        group2.remove(*[dots[i] for i in range(8,13)])
        group1.add(*[dots[i] for i in range(8,13)])

        self.play(Write(creditstext[1]), group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 3), group2.animate.set_color(color.RED).shift(LEFT * 0.125), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 8))
        self.play(FadeOut(creditstext[1]))

        group1.remove(*[dots[i] for i in range(8,13)])
        group2.add(*[dots[i] for i in range(8,13)])
        group2.remove(*[dots[i] for i in [0,1,2,13,14,15]])
        group1.add(*[dots[i] for i in [0,1,2,13,14,15]])

        self.play(Write(creditstext[2]), group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 4), group2.animate.set_color(color.RED).shift(LEFT * 0.25), t1.animate.shift(UP * 0.5), t2.animate.shift(DOWN * 0.5), t3.animate.shift(UP * 0.5), t4.animate.shift(DOWN * 0.5))
        self.play(group1.animate.shift(DOWN * 0.25 * 5))
        self.play(FadeOut(creditstext[2]))

        bigSquare = SurroundingRectangle(alldots, color.YELLOW)
        smallSquare = Square(color = color.YELLOW).scale(0.25).next_to(group1, UP, buff= 0.05)
        # smallSquare.next_to(group1, UP)
        self.play(Write(creditstext[3]), DrawBorderThenFill(bigSquare))
        self.wait(1)
        self.play(FadeOut(creditstext[3]), DrawBorderThenFill(smallSquare))

        self.play(Write(creditstext[4],run_time=4))
        self.wait(2)
        self.play(FadeOut(creditstext[4]))

        self.play(Write(creditstext[5]))
        self.wait(1)
        self.play(FadeOut(creditstext[5]))

        self.play(Write(creditstext[6]))
        self.wait(1)
        self.play(FadeOut(creditstext[6]))

        self.play(Write(creditstext[7]))
        self.wait(1)
        self.play(FadeOut(creditstext[7]))

        self.play(FadeIn(Square().scale(10).set_fill(color.BACKGROUND).set_opacity(1)))


