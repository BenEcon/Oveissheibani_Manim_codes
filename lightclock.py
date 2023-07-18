from manim import *
import numpy as np

class lightclock(Scene):
    def construct(self):
        text=Text("A light clock is a universal based defined clock", width=self.camera.frame_width *0.9).shift(UP*3)
        self.play(Write(text))

        self.t_offset = 0
        colors = color_gradient([YELLOW, RED], 2)

        def update_time(mob, dt):
            self.t_offset += dt
        clock=self.create_light_clock(v=2, A=6, freq=10, sigma=0.1, name="wave", range=4)
        dummy = Mobject()
        dummy.add_updater(update_time)
        self.add(dummy,clock)
        self.wait(3)
        dummy.remove_updater(update_time)




    def create_light_clock(self,v, A, freq, sigma, name, range):
        def update_objects():
            def cos_func(t):
                t0 = np.sin(self.t_offset * v)
                phase = (t + t0) * freq
                superposition = A * np.exp(-(t-t0)**2 / (2*sigma**2)) * (0.02) * np.sin(phase)
                return superposition
            wave= FunctionGraph(lambda t: cos_func(t), x_range=(-range, range), color=rgb_to_color([138/255, 43/255, 226/255])).shift(DOWN*3)
            return VGroup(wave)
        return always_redraw(update_objects)
        
       


