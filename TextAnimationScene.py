from manim import *
import textwrap

class TextAnimationScene(Scene):
    def construct(self):
        # Define the texts and corresponding wait times
      #  texts = [
       #     "We understood time by periodic motions in nature such Day and nigh and seasons",
        #    "Mechanical clocks were invented around 1200 BC For the first time we could measure time",
         #   "Mechanical clocks' operation is based on periodic motion of pendulum or balance wheel"]
            
        exts = [
            "Synchronization of clocks is a method used to ensure that two or more clocks, potentially separated by a significant distance, are measuring time the same way, even if they're moving relative to one another.
            ""]
        waitarray = [10]

        # Define the images and corresponding positions
        images = ["", "", "image3.png"] # Array with empty image names
        img_locations = [RIGHT, RIGHT, 2*DOWN]

        # Call the method
        self.add_texts_and_images(UP + LEFT, texts, waitarray, images, img_locations)

    def add_texts_and_images(self, location, texts, waitarray, images, img_locations):
        text_objs = []
        prev_text = None
        for i, text in enumerate(texts):
            # Wrap the text to a maximum width of 50 characters
            wrapped_text = textwrap.fill(text, width=60)

            # Create the text object
            text_obj = Text(wrapped_text).scale(0.7)

            # Position it below the previous text, or at the chosen side if it's the first
            if prev_text is None:
                text_obj.to_corner(location)
            else:
                text_obj.next_to(prev_text, 2*DOWN).align_to(prev_text, LEFT)

            # Add the text object to the list
            text_objs.append(text_obj)

            # Remember this text object for the next iteration
            prev_text = text_obj

            # Animate the text
            self.play(Write(text_obj))

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
