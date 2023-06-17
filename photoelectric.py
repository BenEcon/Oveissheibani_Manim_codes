from manim import *
import numpy as np

class Photo(Scene):
    def construct(self):
    
       text=Text("At the level of absorbtion and emmision wave becomes particle like",width=self.camera.frame_width *0.9).shift(UP*3)
       #self.add(text)
       self.t_offset = 0
       colors = color_gradient([YELLOW, RED], 2)

       def cos_func(t, A, freq, sigma,stop):
            # Original wave
            wave = A *(0.02)* np.sin((t+self.t_offset) * freq)
            #wave =0
    
            # Center of Gaussian
            t0 = self.t_offset
            Gaussian_packet=0
            # Gaussian wave packet
            t0 = (self.t_offset*3)-5
            if t0<stop:
                Gaussian_packet = A * np.exp(-(t-t0)**2 / (2*sigma**2))
            if t0>stop:
                Gaussian_packet = A * np.exp(-(t-stop)**2 / (2*sigma**2))
    
            # Superposition of the two waves
            superposition =  Gaussian_packet +wave
    
            return superposition
  
       wave1= always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.5,15,0.4,4.5),x_range=(-4,4), color=rgb_to_color([138/255,43/255,226/255])).shift(UP*2))
       wave2= always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,0.5,5,0.4,4.5),x_range=(-4,4), color=GREEN))
       wave3= always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,2,5,0.4,4.5),x_range=(-4,4), color=GREEN).shift(DOWN*2))
      
      
       self.add(wave2,wave1,wave3)
       
     
       def update_time(mob,dt):
            self.t_offset += dt
            
       dummy = Mobject()
       dummy.add_updater(update_time)
       self.add(dummy)
       self.wait(10)
       self.t_offset=0
       self.wait(10)
       dummy.remove_updater(update_time)
       self.wait(10)
    
