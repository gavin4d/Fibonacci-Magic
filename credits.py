from manim import *
import color

class Credits(MovingCameraScene):

    def construct(self):

        self.camera.background_color = color.BACKGROUND
        dots = [Dot().set_color(color.RED).move_to(UP * 0.25 * (10-i)) for i in range(0,21)]

        creditsbox = Rectangle(color=BLACK, fill_opacity= 1, width= 5, height=7.5)
        creditsbox.shift(RIGHT * 6)
        creditsborder = SurroundingRectangle(creditsbox, color=color.YELLOW, buff=0)

        lineSpace = 3.75

        creditstext = [VGroup(
          Text("Thanks for watching!")).arrange(DOWN * lineSpace),
          VGroup(
          Text("A big thank you to"),
          Text("Grant Sanderson"),
          Text("of 3Blue1Brown"),
          Text("for inspiring us"),
          Text("to make"),
          Text("this video.")).arrange(DOWN * lineSpace),
          VGroup(
          Text("Phi Guys are an"),
          Text("entirely"),
          Text("original creation,"),
          Text("and not to be"),
          Text("confused with"),
          Text("Pi Guys.")).arrange(DOWN * lineSpace),
          VGroup(
          Text("No Phi Guys"),
          Text("or Pi Guys"),
          Text("were harmed"),
          Text("in the creation"),
          Text("of this video.")).arrange(DOWN * lineSpace),
          VGroup(
          Text("Animations created"),
          Text("with Manim."),
          Text("Thanks to everyone"),
          Text("in the"),
          Text("Manim community for"),
          Text("making such a"),
          Text("great math animation"),
          Text("library!")).arrange(DOWN * lineSpace),
          VGroup(
          Text("Music:\n"
               "\"Dolphin-esque\"\n"
               "    by Godmode\n"
               "\"Wind Riders\"\n"
               "    by Asher Fulero\n"
               "\"Sunrise in Paris\"\n"
               "    by Dan Henig", line_spacing=lineSpace-1.5),).arrange(DOWN * lineSpace),
          VGroup(
          Text("Don't forget to"),
          Text("like and subscribe!")).arrange(DOWN * lineSpace),
          VGroup(
          Text("Stay tuned"),
          Text("for future videos!")).arrange(DOWN * lineSpace)]

        for i in creditstext:
             i.scale(0.5).move_to(creditsbox)

        alldots = VGroup()
        alldots.add(*[dots[i] for i in range(0,21)])

        self.add(creditsbox, creditsborder)

        self.camera.frame.move_to(RIGHT * 3)

        self.play(Write(creditstext[0]), GrowFromCenter(dots[0]), GrowFromCenter(dots[1]), GrowFromCenter(dots[2]), GrowFromCenter(dots[3]), GrowFromCenter(dots[4]), GrowFromCenter(dots[5]), GrowFromCenter(dots[6]), GrowFromCenter(dots[7]), GrowFromCenter(dots[8]), GrowFromCenter(dots[9]), GrowFromCenter(dots[10]), GrowFromCenter(dots[11]), GrowFromCenter(dots[12]), GrowFromCenter(dots[13]), GrowFromCenter(dots[14]), GrowFromCenter(dots[15]), GrowFromCenter(dots[16]), GrowFromCenter(dots[17]), GrowFromCenter(dots[18]), GrowFromCenter(dots[19]), GrowFromCenter(dots[20]))

        group1 = VGroup()
        group1.add(*[dots[i] for i in range(0,8)])
        group2 = VGroup()
        group2.add(*[dots[i] for i in range(8,21)])

        self.play(group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125), group2.animate.shift(LEFT * 0.125))
        self.play(group1.animate.shift(DOWN * 0.25 * 13))
        self.play(FadeOut(creditstext[0]))

        group1.remove(*[dots[i] for i in range(0,8)])
        group2.add(*[dots[i] for i in range(0,8)])
        group2.remove(*[dots[i] for i in range(8,13)])
        group1.add(*[dots[i] for i in range(8,13)])

        self.play(Write(creditstext[1]), group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 3), group2.animate.set_color(color.RED).shift(LEFT * 0.125))
        self.play(group1.animate.shift(DOWN * 0.25 * 8))
        self.play(FadeOut(creditstext[1]))

        group1.remove(*[dots[i] for i in range(8,13)])
        group2.add(*[dots[i] for i in range(8,13)])
        group2.remove(*[dots[i] for i in [0,1,2,13,14,15]])
        group1.add(*[dots[i] for i in [0,1,2,13,14,15]])

        self.play(Write(creditstext[2]), group1.animate.set_color(color.BLUE).shift(RIGHT * 0.125 * 4), group2.animate.set_color(color.RED).shift(LEFT * 0.25))
        self.play(group1.animate.shift(DOWN * 0.25 * 5))
        self.play(group1.animate.set_color(color.RED), FadeOut(creditstext[2]))
        self.play(alldots.animate.scale(2).shift(UP * 2))

        bigSquare = SurroundingRectangle(alldots, color.RED)
        smallSquare = Square(color=color.BLUE).scale(0.43).next_to(group1, UP, buff=0.14)

        self.play(Write(creditstext[3]), DrawBorderThenFill(bigSquare))
        self.wait(1)
        self.play(FadeOut(creditstext[3]), DrawBorderThenFill(smallSquare))

        self.play(Write(creditstext[4], run_time=4))
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


