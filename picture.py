from manim import *
from pathlib import Path

class MyScene(Scene):
    def construct(self):
        # ... your other code ...
        self.add_picture("H_A_Lorentz_(Nobel).jpg", LEFT*4+UP*2,2*RIGHT, "Lorentz transformations", "Hendrik Lorentz", "1853", "1928")
        self.wait(10)
        
        self.add_picture("Henri_Poincaré-2.jpg", LEFT*4+DOWN*2,2*RIGHT, "Invariances of transformations", "Henri Poincaré", "1854", "1912")
        self.wait(10)
        
        # ... your other code ...

    def add_picture(self, pic_name, location,textloc,description, title, start_date, end_date):
        # Load the image
        img = ImageMobject(pic_name)
        
        # Scale it to the height of the scene and then scale by 0.5
        img.height = self.camera.frame_height - 1
        img.scale(0.5)

        # Move it to the chosen location
        img.move_to(location)

        # Create the title
        title_text = Text(title).scale(0.7).next_to(img, textloc)

        # Create the date range text
        date_text = Text(f" {start_date} - {end_date}").scale(0.7).next_to(title_text, DOWN * 0.2)

        # Create the description
        desc_text = Text(description).scale(0.7).next_to(date_text, DOWN * 0.2)
        
        # Align texts along x-axis
        for t in [date_text, desc_text]:
            t.align_to(title_text, LEFT)
        
        # Add the elements to the scene one by one
        self.play(FadeIn(img))
        self.play(Write(title_text))
        self.play(Write(date_text))
        self.play(Write(desc_text))

        return img, title_text, date_text, desc_text
