from manim import *

class ether(Scene):
    def construct(self):
        self.t_offset = 0
        def update_time(mob, dt):
            self.t_offset += dt



        # Pass the desired v value to the function
        v=0
        moving_objects = self.create_moving_objects(v=v,y=1.5,A=0.1,freq=30)
        v=0.25
        moving_objects1 = self.create_moving_objects(v=v,y=0.5,A=0.1,freq=10)
        v=0.5
        moving_objects2 = self.create_moving_objects(v=v,y=-0.5,A=0.1,freq=5)
        v=1
        moving_objects3 = self.create_moving_objects(v=v,y=-1.5,A=0.1,freq=0)
        
        dummy = Mobject()
        dummy.add_updater(update_time)
        self.add(dummy, moving_objects, moving_objects1, moving_objects2,moving_objects3)
        self.wait(15)

    def create_moving_objects(self, v, y, A, freq):
        def update_objects():
            center = np.array([-6.65+self.t_offset * v * 0.2, y, 0]) + (UP * y)  # Update center using v
            center_Wave=np.array([4, y, 0]) + (UP * y)  # Update center using v
            def light(t):
                return A * np.sin(20*(t)+self.t_offset*freq)
            
            dot = Dot(center)
            h_arrow = Arrow(start=center, end=center + RIGHT, color=RED, buff=0)
            v_arrow = Arrow(start=center, end=center + UP, color=BLUE, buff=0)
            wave = FunctionGraph(lambda t: light(t), x_range=(-1,+1), color=YELLOW).shift(center_Wave+UP*0.3)
            rect = Rectangle(width=4, height=10*A).move_to(wave).set_fill(BLUE, opacity=0.4)
            ether_text = Text("Ether").move_to(rect).shift(UP*0.3+LEFT).scale(0.5)
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





class michelson(Scene):
    def construct(self):
        self.t_offset = 0
        def update_time(mob, dt):
            self.t_offset += dt



        # Pass the desired v value to the function
        v=0
        moving_objects = self.create_moving_objects(A=0.1,freq=30,phase=0)
        #moving_objects1 = self.create_moving_objects(A=0.1,freq=30,phase=2)
        
        
        time=20
        dummy = Mobject()
        dummy.add_updater(update_time)
        self.add(dummy, moving_objects)
        self.wait(time)

    def create_moving_objects(self, A, freq,phase):
       
        
        
        def update_objects():
            phase= self.t_offset
            phase2=phase/np.pi
            circle = Circle(radius=0.5, color=WHITE).shift(4*RIGHT+UP*0.8)
            arrow = Arrow(circle.get_center(), circle.point_at_angle(phase), color=YELLOW)
            
            def light(t):
                return A * np.sin(20*(t)+self.t_offset*freq)
            def light2(t):
                return A * np.sin(20*(t)+(self.t_offset*freq)+phase)
                
            def sum(t):
                return light(t) + light2(t)
                
            range=6
            wave = FunctionGraph(lambda t: light(t), x_range=(-range,range), color=RED).shift(UP*2)
            wave_text = Text("Wave parallel to earth speed").next_to(wave, UP*0.5).scale(0.5)

            wave2 = FunctionGraph(lambda t: light2(t), (-range,range), color=GREEN)
            wave2_text = Text("Wave perpendicular to earth speed").next_to(wave2, UP*0.5).scale(0.5)

            wave3 = FunctionGraph(lambda t: sum(t), (-range,range), color=BLUE).shift(DOWN*2)
            wave3_text = Text("Superposition").next_to(wave3, UP*0.5).scale(0.5)

# add the Text objects to the VGroup
            

         #   end_line = Line(start=(-10, wave.get_center()[1], 0)+DOWN*0.5, end=(10, wave.get_center()[1], 0)+DOWN*0.5, color=GREY)
            phase_text = MarkupText(f'<span foreground="{RED}">phase shift</span> / <span foreground="{ORANGE}">π</span> = <span foreground="{YELLOW}">{phase2:.2f}</span>', font="Times New Roman").move_to(wave2.get_center()).shift(UP).scale(0.5)

            return VGroup(wave, wave_text, wave2, wave2_text, wave3, wave3_text, phase_text,circle,arrow)

        return always_redraw(update_objects)

