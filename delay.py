from manim import *
import numpy as np

class delay(Scene):
    def construct(self):
        text=Text("A light clock is a universal based defined clock", width=self.camera.frame_width *0.9).shift(UP*3)
        #self.play(Write(text))

        self.t_offset = 0
        colors = color_gradient([YELLOW, RED], 2)

        def update_time(mob, dt):
            self.t_offset += dt
            
        clock=self.create_bouncing_dot(v=0.1,c=1,L=0.5,location=2*UP+LEFT*3,correction=0.4)
        clock1=self.create_bouncing_dot(v=0.5,c=1,L=0.5,location=LEFT*3,correction=0.4)
        clock2=self.create_bouncing_dot(v=0.8,c=1,L=0.5,location=2*DOWN+LEFT*3,correction=0.4)
        
        dummy = Mobject()
        dummy.add_updater(update_time)
        self.add(dummy,clock,clock1,clock2)
        self.wait(30)
        dummy.remove_updater(update_time)
       
       

    def create_bouncing_dot(self, v, c, L, location,correction):
    
        moving_dot = Dot(radius=0.1).set_fill(RED)
        path = TracedPath(moving_dot.get_center, stroke_width=2).set_fill(RED)
        
        def update_objects():
            ypos1 = L * np.sin(np.sqrt(c**2 - v**2) * self.t_offset*correction)
            #ypos1 = L * np.sign(np.sin(np.sqrt(c**2 - v**2) * self.t_offset))
            xpos = v * self.t_offset *correction
            end_point = np.array([xpos, ypos1, 0]) + location
            moving_dot.move_to(end_point)
            circle = Circle(radius=0.5, color=WHITE).shift(location+LEFT*2).set_fill(color=WHITE, opacity=1)
            arrow = Arrow(circle.get_center(), circle.point_at_angle(-np.sqrt(c**2 - v**2) * self.t_offset), color=BLACK)
            formatted_V= "{:.2f}".format(v)
            equation = "v/c= "+formatted_V
            v_text = MathTex(equation).shift(location+DOWN)
            rectangle = Rectangle(height=1, width=L/2).shift(location+[xpos,0,0]).set_fill(YELLOW, opacity=0.2)
            
            
            
        # Add a TracedPath to the moving dot
            

            return VGroup(moving_dot, path,circle,arrow,v_text,rectangle)

        return always_redraw(update_objects)
