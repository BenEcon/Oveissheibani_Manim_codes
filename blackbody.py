from manim import *
import numpy as np

class BlackBody(Scene):
    def construct(self):
    
       text=Text("There is no limit in adding energy to a black body",width=self.camera.frame_width *0.9).shift(UP*3)
       #self.add(text)
       self.t_offset = 0
       rect=Rectangle(width=4.0, height=2.0).set_fill(color=BLACK, opacity=1)# grid_xstep=1.0, grid_ystep=0.5)
       num_circles = 6
       colors = color_gradient([YELLOW, RED], num_circles)
       circles = VGroup(*[
            Circle().set_stroke(color=color, width=2) for color in colors
       ])
       #for i, circle in enumerate(circles):
       #circle.scale((i)*0.5).shift(2*LEFT)  # Make each circle a bit bigger than the last
       #self.add(circle)
       radiation= AnnularSector(inner_radius=3, outer_radius=4, angle=np.pi*2, start_angle=0, fill_opacity=1, stroke_width=0, color=RED)
       vertices = rect.get_vertices()
       bottom_left = vertices[0]
       top_left = vertices[1]
       top_right = vertices[2]
       bottom_right = vertices[3]
       middle_right=(vertices[2]+vertices[3])/2
       middle_left=(vertices[0]+vertices[1])/2
       def cos_func(t, A, freq, k):
            return A * np.sin(k * np.pi/2 * t) * np.cos((self.t_offset) * freq)

       wave1= always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,20,20),x_range=(-2,+2), color=BLUE).shift(UP*0.1))
       wave2=always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,8,8),x_range=(-2,+2), color=YELLOW).shift(DOWN*0.1))
       wave3=always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,1,1),x_range=(-2,+2), color=RED).shift(DOWN*0.2))
       
#       wave1= always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,A=2),x_range=(-2,+2), color=PURPLE))
#       wave2=always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,A=4),x_range=(-2,+2), color=YELLOW))
       self.add(rect)

       
       wave4= always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,12,12),x_range=(-2,+2), color=PINK).shift(DOWN*0.3))
       wave5=always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,16,16),x_range=(-2,+2), color=GREEN).shift(DOWN*0.4))
       wave6=always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,4,4),x_range=(-2,+2), color=ORANGE).shift(DOWN*0.5))
       wave7=always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,24,24),x_range=(-2,+2), color=rgb_to_color([138/255,43/255,226/255])).shift(DOWN*0.6))
       
       math1=MathTex(r"u(\nu)=\frac{8 \pi \nu^2}{c^3} \bar{E} ").shift(UP*2+RIGHT*3.5)
       math2=MathTex(r"= \frac{8 \pi \nu^2 k T}{c^3}",color=RED).shift(UP*0+RIGHT*3.5)
       math3=MathTex(r"\bar{E}=\frac{h \nu}{\mathrm{e}^{h \nu / k T}-1}",color=GREEN).shift(UP*(-2)+RIGHT*3.5)

       num1=2


       def update_time(mob,dt):
            self.t_offset += dt
       dummy = Mobject()
       dummy.add_updater(update_time)
       self.add(dummy)
       self.add(wave1)
       self.wait(num1)
       self.add(wave2)
       self.wait(num1)
       self.add(wave3)
       self.wait(num1)
       self.add(wave4)
       self.wait(num1)
       self.add(wave5)
       self.wait(num1)
       self.add(wave6)
       self.wait(num1)
       self.add(wave7)
       self.wait(num1)
       self.wait(10)
#       self.add(math1)
#       self.wait(3)
#       self.add(math2)
#       self.wait(3)
#       self.add(math3)
#       self.wait(num2)
       dummy.remove_updater(update_time)

class TextOfBlackBody(ThreeDScene):
    def construct(self):
        
        text1=Text("Rayleigh–Jeans law:",width=self.camera.frame_width *0.9).shift(UP*3)
        lagrangian=MathTex(r"B_\nu(T)=\frac{2 \nu^2 k_{\mathrm{B}} T}{c^2}")


        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        k = ValueTracker(2)
        dk = 0.1 # Differential thickness

        # Define the function for the angular sector of a sphere
        def func(u, v):
            theta = u * 2 * PI  # Angle around sphere (0 to 2pi)
            phi = v * PI  # Angle down from pole (0 to pi)
            r = k.get_value() + dk * v  # Radius varies from k to k + dk
            return np.array([r * np.sin(phi) * np.cos(theta), r * np.sin(phi) * np.sin(theta), r * np.cos(phi)])

        # Create the 3D surface
        sector = always_redraw(
            lambda: Surface(
                func,
                u_range=[0, 1],
                v_range=[0, 1],
                checkerboard_colors=[BLUE_D, BLUE_E],
                resolution=(6, 6),
            )
        )

        # Create the label for k
        k_label = DecimalNumber(k.get_value(), num_decimal_places=1)
        k_label.add_updater(lambda m: m.set_value(k.get_value()))
        k_text = Tex("k = ").next_to(k_label, LEFT)
        k_display = VGroup(k_text, k_label).to_corner(UL)

        # Create the 3D arrow
        def arrow_endpoint():
            center = sector.get_center()
            direction = center - ORIGIN
            distance = np.linalg.norm(direction)
            direction_normalized = direction / distance
            desired_distance = distance - 0.2  # Replace 0.2 with the desired 'buff' distance
            return ORIGIN + direction_normalized * desired_distance

        arrow = always_redraw(lambda: Arrow3D(ORIGIN, arrow_endpoint(), color=YELLOW))

        self.add(sector, arrow, k_display)

        # Change the value of k over time
        self.play(k.animate.set_value(2.5))
        self.wait()
