from manim import *

class frame_3(Scene):
    def construct(self):
        self.t_offset = 0
        def update_time(mob, dt):
            self.t_offset += dt



        # Pass the desired v value to the function
        v=0
        moving_objects = self.create_moving_objects(v=v,y=1.5,A=0.1,freq=30)
        v=0.25
        moving_objects1 = self.create_moving_objects(v=v,y=0.5,A=0.1,freq=30)
        v=0.75
        moving_objects2 = self.create_moving_objects(v=v,y=-0.5,A=0.1,freq=30)
        v=1
        moving_objects3 = self.create_moving_objects(v=v,y=-1.5,A=0.1,freq=30)
        
        dummy = Mobject()
        dummy.add_updater(update_time)
        self.add(dummy, moving_objects, moving_objects1, moving_objects2,moving_objects3)
        self.wait(1)

    def create_moving_objects(self, v, y, A, freq):
        def update_objects():
            center = np.array([-6.65+self.t_offset * v * 0.3, y, 0]) + (UP * y)  # Update center using v
            
            def light(t):
                return A * np.sin(20*(t)+self.t_offset*freq)
            
            dot = Dot(center)
            h_arrow = Arrow(start=center, end=center + RIGHT, color=RED, buff=0)
            v_arrow = Arrow(start=center, end=center + UP, color=BLUE, buff=0)
            wave = FunctionGraph(lambda t: light(t), x_range=(-1,+1), color=YELLOW).shift(2*UP*y+RIGHT*4.5)
            rect = Rectangle(width=4, height=10*A).move_to(wave).set_fill(BLUE, opacity=0.4)
            ether_text = Text("Ether").move_to(rect).shift(UP*0.4+LEFT*0.6).scale(0.5)
            speed_text = MathTex(f"\\text{{speed}}/\\text{{speed of light}} = {v}").next_to(dot, UP+RIGHT*1.5)
            
            
            end_line = Line(start=(-10, dot.get_center()[1], 0)+DOWN*0.5, end=(10, dot.get_center()[1], 0)+DOWN*0.5, color=GREY)

            return VGroup(dot, h_arrow, v_arrow, wave, speed_text, end_line,rect,ether_text)

        return always_redraw(update_objects)




class GalileanTransformations(Scene):
    def construct(self):
        # Write down the Galilean transformations
        eq1 = MathTex("x' = x - vt")
        eq2 = MathTex("t' = t")

        # Position equations
        eq1.shift(UP)
        eq2.shift(DOWN)

        # Animate
        self.play(Write(eq1))
        self.wait(5)
        self.play(Write(eq2))
        self.wait(5)
