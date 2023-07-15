from manim import *
import textwrap
import numpy as np

class synchro(Scene):
    def construct(self):
        # Define the texts and corresponding wait times
        texts = ["Synchronization of clocks is a method used to ensure that two or more clocks, potentially separated by a significant distance, are measuring time the same way, even if they're moving relative to one another."]
        equations = ["t = t^{\\prime}"]
        waitarray = [10]
        self.t_offset=0
        def update_time(mob, dt):
            self.t_offset += dt
        # Define the images and corresponding positions
        images = ["", "", ""] # Array with empty image names
        img_locations = ["", "", ""]
 
        n = 12  # Total number of clocks
        sync_time = 0  # Time at which all clocks should be synchronized

        # Generate the initial phases, uniformly spread between 0 and 2π
        initial_phases = np.linspace(0, 6*np.pi-np.pi/2, n)

        # Calculate the delays such that all clocks will be in sync at sync_time
        # The delay for a clock is essentially the time it would need to "wait" before starting,
        # such that it will reach the same phase as all other clocks at sync_time.
        # Assuming that the phase increases linearly with time, the delay can be calculated as:
        delays = initial_phases

        # Calculate the x_positions so that the clocks are uniformly spread on the x-axis
        x_positions = np.linspace(-5, 5, n)  # Adjust -5 and 5 as per your requirements



        dummy = Mobject()
        self.add(dummy)
        dummy.add_updater(update_time)
 #Now you can pass these values into your `create_clock` function
        for i in range(n):
            clock = self.create_clock(1, initial_phases[i], delays[i], x_positions[i])
            self.add(clock)
 
        ax = self.create_axis(n, x_positions, y_location=0, title="frame_1")
        self.add(ax)
        self.add_texts_and_images(UP + LEFT, texts,equations ,waitarray, images, img_locations)
        
        
        
        self.wait(1)
        
        

    def add_texts_and_images(self, location, texts,equations, waitarray, images, img_locations):
        text_objs = []
        prev_text = None
        for i, text in enumerate(texts):
            # Wrap the text to a maximum width of 50 characters
            wrapped_text = textwrap.fill(text, width=60)

            # Create the text object
            text_obj = Text(wrapped_text).scale(0.7)
            equation_obj=MathTex(equations[i])
            
            # Position it below the previous text, or at the chosen side if it's the first
            if prev_text is None:
                text_obj.to_corner(location)
            else:
                text_obj.next_to(prev_text, 2*DOWN).align_to(prev_text, LEFT)

            # Add the text object to the list
            text_objs.append(text_obj)

            # Remember this text object for the next iteration
            prev_text = text_obj
            equation_obj.next_to(text_obj, 0.5* DOWN+RIGHT*0.3)

            # Animate the text
            self.play(Write(text_obj))
            self.play(Write(equation_obj))

            # If there are images and the image name is not empty, animate the corresponding image
            if images and i < len(images) and images[i]:
                # Load the image
                img = ImageMobject(images[i])

                # Scale and position it
                img.height = self.camera.frame_height - 4
                img.scale(0.6)
                img.next_to(text_obj, img_locations[i])
                self.wait(waitarray[i])
                # Animate the image
                self.play(FadeIn(img))

        return text_objs


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
        

#
#    def create_axis(self, leng, y_location, n, title):
#        x_min, x_max, x_step = 0, 10, 1
#
#        def update_objects():
#            x_range = np.linspace(0, leng, n)
#            axis = NumberLine(x_range=[x_min, x_max, x_step]).shift([0, y_location, 0])
#            title_text = Text(title).set_color(YELLOW).next_to(axis, UP)
#            return VGroup(axis, title_text)
#
#        return always_redraw(update_objects)
    def create_axis(self, n, positions, y_location=0, title=""):
        x_min, x_max = min(positions), max(positions)

        def update_objects():
            axis = NumberLine(x_range=[x_min, x_max, (x_max-x_min)/n]).shift([0, y_location, 0])
            title_text = Text(title).set_color(YELLOW).next_to(axis, UP)
            return VGroup(axis, title_text)

        return always_redraw(update_objects)
