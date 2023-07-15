from manim import *
import textwrap

class TextAnimationScene(Scene):
    def construct(self):
        # Define the texts and corresponding wait times
        texts = ["The period of oscillation for a simple hormonic oscillator does not change by frame velocity. "]
        equations = ["t = t^{\\prime}"]
        waitarray = [10]
        self.t_offset=0
        def update_time(mob, dt):
            self.t_offset += dt
        # Define the images and corresponding positions
        images = ["", "", ""] # Array with empty image names
        img_locations = [RIGHT, RIGHT, 2*DOWN]
        cube= self.create_moving_cube(20, 2, 6)
        cube1= self.create_moving_cube(10, 2, 6)
        # Call the method
        self.add_texts_and_images(UP + LEFT, texts,equations ,waitarray, images, img_locations)
        dummy = Mobject()
        dummy.add_updater(update_time)
        self.add(dummy,cube)
        self.wait(15)
        self.remove(cube)
        self.add(cube1)
        self.wait(10)
        
        

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
