from manim import *
import textwrap
import numpy as np

class einstein(Scene):
    def construct(self):
        # Define the texts and corresponding wait times
        texts = ["How Einstein reformulated the problem?", "1. The speed of light is the same in all frame of refrence unlike anything else massive ", "2. The laws of physics are the same in all non accelating frames of refrence and there is no need to an stationary frame or Ether"
        ]
        equations = []
        waitarray = [10,10,10]
        self.t_offset=0
        def update_time(mob, dt):
            self.t_offset += dt
        # Define the images and corresponding positions
        images = ["", "", ""] # Array with empty image names
        img_locations = ["", "", ""]
        self.add_texts_and_images(UP + LEFT, texts,equations ,waitarray, images, img_locations)
    
   

        dummy = Mobject()
        self.add(dummy)
        dummy.add_updater(update_time)

        
        

    def add_texts_and_images(self, location, texts,equations, waitarray, images, img_locations):
        text_objs = []
        prev_text = None
        for i, text in enumerate(texts):
            # Wrap the text to a maximum width of 50 characters
            wrapped_text = textwrap.fill(text, width=60)

            # Create the text object
            text_obj = Text(wrapped_text).scale(0.7)
            #equation_obj=MathTex(equations[i])
            
            # Position it below the previous text, or at the chosen side if it's the first
            if prev_text is None:
                text_obj.to_corner(location)
            else:
                text_obj.next_to(prev_text, 4*DOWN).align_to(prev_text, LEFT)

            # Add the text object to the list
            text_objs.append(text_obj)

            # Remember this text object for the next iteration
            prev_text = text_obj
            #equation_obj.next_to(text_obj, 0.5* DOWN+RIGHT*0.3)

            # Animate the text
            self.play(Write(text_obj))
            #self.play(Write(equation_obj))
            self.wait(waitarray[i])
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
