from manim import *
import numpy as np

class light(Scene):
    def construct(self):
        text=Text("At the level of absorption and emission wave becomes particle-like", width=self.camera.frame_width *0.9).shift(UP*3)
        self.play(Write(text))

        self.t_offset = 0
        colors = color_gradient([YELLOW, RED], 2)
        self.last_phase_rounded = {}

        ref_point = 3*LEFT

        def cos_func(t, A, freq, sigma, speed, name):
            counter = ValueTracker(0)
            counter_text = DecimalNumber(counter.get_value(), num_decimal_places=0).next_to(ref_point, UP)

            if name not in self.last_phase_rounded:
                self.last_phase_rounded[name] = 0

            t0 = np.sin(self.t_offset * speed)
            phase = (t + t0) * freq
            phase_rounded = round(phase / np.pi)

            if phase_rounded != self.last_phase_rounded[name]:
                self.last_phase_rounded[name] = phase_rounded
                counter.increment_value(1)
            
            superposition = A * np.exp(-(t-t0)**2 / (2*sigma**2)) * (0.02) * np.sin(phase)
            return superposition, counter_text

        wave1 = always_redraw(lambda: FunctionGraph(lambda t: cos_func(t, 50, 15, 0.4, 5, "wave1")[0], x_range=(-4, 4), color=rgb_to_color([138/255, 43/255, 226/255])).shift(UP*2))
        counter_text1 = always_redraw(lambda: cos_func(0, 50, 15, 0.4, 5, "wave1")[1])

        self.add(wave1, counter_text1)

        def update_time(mob, dt):
            self.t_offset += dt
    
        dummy = Mobject()
        dummy.add_updater(update_time)
        self.add(dummy)
        self.wait(5)
        dummy.remove_updater(update_time)
