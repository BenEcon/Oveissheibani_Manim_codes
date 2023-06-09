from manim import *
import numpy as np

class BlackBody(Scene):
    def construct(self):
    
       text=Text("There is no limit in adding energy to black body",width=self.camera.frame_width *0.9).shift(UP*3)
       self.add(text)
       self.t_offset = 0
       rect=Rectangle(width=4.0, height=2.0).set_fill(color=BLACK, opacity=1).shift(LEFT*2)# grid_xstep=1.0, grid_ystep=0.5)
       num_circles = 6
       colors = color_gradient([YELLOW, RED], num_circles)
       circles = VGroup(*[
            Circle().set_stroke(color=color, width=2) for color in colors
       ])
       vertices = rect.get_vertices()
       bottom_left = vertices[0]
       top_left = vertices[1]
       top_right = vertices[2]
       bottom_right = vertices[3]
       middle_right=(vertices[2]+vertices[3])/2
       middle_left=(vertices[0]+vertices[1])/2
       def cos_func(t, A, freq, k):
            return A * np.sin(k * np.pi/2 * t) * np.cos((self.t_offset) * freq)

       wave1= always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,30,30),x_range=(-2,+2), color=BLUE).shift(LEFT*2))
       wave2=always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,12,12),x_range=(-2,+2), color=YELLOW).shift(DOWN*0.1+LEFT*2))
       wave3=always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,5,5),x_range=(-2,+2), color=RED).shift(DOWN*0.2+LEFT*2))
       
#       wave1= always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,A=2),x_range=(-2,+2), color=PURPLE))
#       wave2=always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,A=4),x_range=(-2,+2), color=YELLOW))
       self.add(rect)

       
       wave4= always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,15,15),x_range=(-2,+2), color=PINK).shift(LEFT*2+DOWN*0.3))
       wave5=always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,20,20),x_range=(-2,+2), color=BLUE_C).shift(DOWN*0.4+LEFT*2))
       wave6=always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,10,10),x_range=(-2,+2), color=ORANGE).shift(DOWN*0.5+LEFT*2))
       wave7=always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.1,40,40),x_range=(-2,+2), color=rgb_to_color([138/255,43/255,226/255])).shift(DOWN*0.6+LEFT*2))
       
       
       num1=1
       num2=1
       
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
       self.wait(num2)
       for i, circle in enumerate(circles):
            circle.scale((i)*0.5).shift(2*LEFT)  # Make each circle a bit bigger than the last
            self.add(circle)
       group=VGroup(*circles)
       self.play(group.animate.scale(1.2),run_time=5)
       dummy.remove_updater(update_time)
            
    
