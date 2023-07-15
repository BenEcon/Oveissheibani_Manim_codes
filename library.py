



    def create_axis(self, n, positions, y_location=0, title=""):
        x_min, x_max = min(positions), max(positions)

        def update_objects():
            axis = NumberLine(x_range=[x_min, x_max, (x_max-x_min)/n]).shift([0, y_location, 0])
            title_text = Text(title).set_color(YELLOW).next_to(axis, UP)
            return VGroup(axis, title_text)

        return always_redraw(update_objects)
        
        
        
        
        
        
        
    def create_moving_cube(self, k, m, A):
 
        freq = np.sqrt(k/m)
        
        def update_objects():
            phase = self.t_offset

        # Periodic function for cube position
            def cube_position(t):
                return A * np.sin(freq * phase)
        
            square = Square().move_to(RIGHT * cube_position(self.t_offset)).scale(0.5)
            square.set_fill(color=[RED, ORANGE], opacity=1)
            line = Line(ORIGIN, square.get_center())
            formatted_freq = "{:.2f}".format(freq)
            equation = "\\omega = \\sqrt{\\frac{k}{m}} = "+formatted_freq
            freq_text = MathTex(equation).shift(DOWN*2)
            circle = Circle(radius=0.5, color=WHITE).shift(UP*0.1).set_fill(color=WHITE, opacity=1)
            arrow = Arrow(circle.get_center(), circle.point_at_angle(-phase), color=BLACK)
            
        # Text showing k and m
      
        
            #self.t_offset += 0.02  # Increment the time offset (adjust speed as needed)

            return VGroup(square, line,freq_text,circle,arrow)

        return always_redraw(update_objects)



    def create_moving_wave(self, A, freq,phase):
       
        
        
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



    def create_moving_frame(self, v, y, A, freq):
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
        
        
        
    def create_clock(self,A,initphase,delay,x):
            
                
            
        def update_objects():
           
           
            phase=-initphase
            if(self.t_offset*0.8<initphase):
                phase=-initphase
            else:
                phase=-self.t_offset*0.8
                
            circle = Circle(radius=0.25, color=WHITE).shift(UP*0.1).set_fill(color=WHITE, opacity=1).shift([x,0,0])
            arrow = Arrow(circle.get_center(), circle.point_at_angle(phase), color=BLACK,buff=0)
            
        # Text showing k and m
      
        
            #self.t_offset += 0.02  # Increment the time offset (adjust speed as needed)

            return VGroup(circle,arrow)

        return always_redraw(update_objects)
        
        
        



