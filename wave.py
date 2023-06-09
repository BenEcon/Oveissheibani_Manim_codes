from manim import *
from manim_physics import *

class DoubleSlitExperiment(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(60 * DEGREES, -45 * DEGREES)
        
        # Position the sources at the location of the "slits"
        slit1 = LEFT * 2 + DOWN * 5
        slit2 = RIGHT * 2 + DOWN * 5

        # Create the waves from the two slits
        wave1 = RadialWave(slit1, checkerboard_colors=[BLUE_D,RED,YELLOW,PURPLE], stroke_width=0, x_range=[-10,10],  # Increase the range of u
            y_range=[-10, 10]
        )
       

        # Add the waves to the scene
        self.add(wave1)

        # Start the waves
     #   wave1.start_wave()
    #    wave2.start_wave()

        # Allow the waves to propagate and interfere
   #     self.wait()

        # Stop the waves
  #      wave1.stop_wave()
  #      wave2.stop_wave()

