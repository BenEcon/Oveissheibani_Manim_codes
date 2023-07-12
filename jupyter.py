from manim import *

class NumberLineScene(Scene):
    def construct(self):
        # Create a NumberLine
        number_line = NumberLine(x_range=[-10,10,1], length=10, include_numbers=False)

        # Create an arrow
        arrow = Arrow(number_line.number_to_point(-10), end=number_line.number_to_point(-10)+RIGHT, buff=0)

        # Create a blue dot
        dot = Dot(point=number_line.number_to_point(-10), color=BLUE)
        # Create the text "Earth"
        earth_text = Text("Earth").next_to(dot, UP)

        # Create a larger yellow dot
        yellow_dot = Dot(point=number_line.number_to_point(10), color=YELLOW, radius=0.4)
        # Create the text "Jupiter"
        jupiter_text = Text("Jupiter").next_to(yellow_dot, UP)

        # Create a brace between the dots
        brace = Brace(Line(dot.get_center(), yellow_dot.get_center()), UP)
        # Create the text "D" above the brace
        D_text = Text("D").next_to(brace, UP)

        # Show the number line, the arrow, the dots, the texts, the brace, and the "D" text
        self.play(Create(number_line), Create(arrow), Create(dot), Write(earth_text), Create(yellow_dot), Write(jupiter_text), Create(brace), Write(D_text))

        # Create the path for the dot to follow
        path = Line(dot.get_center(), number_line.number_to_point(10))
        # Move the dot along the path
        #self.play(MoveAlongPath(dot,arrow, path, rate_func=linear), run_time=20)

        # Update the position of the Earth text and the brace
        #self.play(earth_text.animate.next_to(dot, UP), brace.animate.become(Brace(Line(dot.get_center(), yellow_dot.get_center()), UP)))

        # Create an arrow starting from yellow dot towards the blue dot
        #yellow_dot_arrow = Arrow(yellow_dot.get_center(), dot.get_center(), buff=0)
        # Show the arrow
        self.play(Create(yellow_dot_arrow))
        
        self.t_offset = 0
        def cos_func(t, A, freq, k):
            return A * np.sin(k * np.pi/2 * t + (self.t_offset) * freq)
        wave2=always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,8,8),x_range=(-5+self.t_offset*0.1,number_line.number_to_point(10)[0]), color=YELLOW))
        def update_time(mob,dt):
            self.t_offset += dt
        dummy = Mobject()
        dummy.add_updater(update_time)
        self.add(dummy,wave2)
        self.play(MoveAlongPath(dot,arrow, path, rate_func=linear), run_time=20)
        # Create the path for the arrow to follow
        #arrow_path = Line(yellow_dot_arrow.get_start(), dot.get_center())
        # Move the arrow along the path
        self.wait(5)
        #self.play(MoveAlongPath(yellow_dot_arrow, arrow_path, rate_func=linear), run_time=5)
        dummy.remove_updater(update_time)
        
        
        
        
        
        
class EquationsScene(Scene):
    def construct(self):
        n=5
        # Create the equations
        equation1 = MathTex("T_1 = \\frac{D}{v + c}").shift(LEFT*n)
        equation2 = MathTex("T_2 = P + \\frac{D - \\frac{Dc}{v+c}}{v + c}").shift(LEFT*n)
        equation3 = MathTex("\\Delta T = P + \\frac{D}{c(1 + \\frac{v}{c})}").shift(LEFT*n)
        equation4 = MathTex("c \\rightarrow \\infty").shift(LEFT*n)
        equation5 = MathTex("\\delta T \\rightarrow P").shift(LEFT*n)

        # Position the equations
        equation1.to_edge(UP)
        equation2.next_to(equation1, DOWN, buff=1)
        equation3.next_to(equation2, DOWN, buff=1)
        equation4.next_to(equation3, RIGHT, buff=1)
        equation5.next_to(equation3, RIGHT*4, buff=1)

        # Display the equations
        self.play(Write(equation1))
        self.wait(3)
        self.play(Write(equation2))
        self.wait(3)
        self.play(Write(equation3))
        self.wait(3)
        self.play(Write(equation4))
        self.wait(3)
        self.play(Write(equation5))
        self.wait(3)
        
        


class EarthSpeed(Scene):
    def construct(self):
        title = Text("Earth's Speed Relative to the Speed of Light")
        speed_earth = 29.78 # in km/s
        speed_light = 299792.458 # in km/s

        earth_text = Text("Earth's Speed: {:.2f} km/s".format(speed_earth))
        light_text = Text("Speed of Light: {:.2f} km/s".format(speed_light))

        ratio = speed_light/speed_earth
        ratio_text = MathTex("c / v = {:.10f}".format(ratio))

        self.play(Write(title))
        self.wait(1)
        self.play(FadeOut(title), Write(earth_text))
        self.wait(1)
        self.play(Transform(earth_text, light_text))
        self.wait(1)
        self.play(Transform(earth_text, ratio_text))
        self.wait(2)

        
