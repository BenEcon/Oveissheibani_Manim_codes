from manim import *
import numpy as np

class light(Scene):
    def construct(self):
    
       text=Text("At the level of absorbtion and emmision wave becomes particle like",width=self.camera.frame_width *0.9).shift(UP*3)
       #self.add(text)
       self.t_offset = 0
       self.counter = ValueTracker(0) # ValueTracker for counter
       counter_text = DecimalNumber(self.counter.get_value(), num_decimal_places=0).add_updater(lambda v: v.set_value(self.counter.get_value())) # Text to display counter
       counter_text.to_corner(LEFT) # Place the text at the top left corner of the screen
       self.add(counter_text) # Add the counter text to the screen
       colors = color_gradient([YELLOW, RED], 2)
 
       def cos_func(t, A, freq, sigma,stop,ref,speed):
            # Original wave
            #wave =0
          
            # Center of Gaussian
      

            # Gaussian wave packet
            t0 = ref*np.sin(self.t_offset*speed)
            epsilon = 0.1  # adjust as needed for your scenario
            if abs(t0 - ref) < epsilon or abs(t0 - (-1*ref)) < epsilon:
                self.counter.increment_value()
            # Superposition of the two waves
            superposition =  A * np.exp(-(t-t0)**2 / (2*sigma**2))*(0.02)* np.sin((t+t0) * freq)
      
    
            return superposition
  
       wave1= always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,50  ,15,0.4,4.5,3,5),x_range=(-4,4), color=rgb_to_color([138/255,43/255,226/255])).shift(UP*2))
   
       self.add(wave1)
       
       
       def update_time(mob,dt):
            self.t_offset += dt
            
         
            
            
            
       dummy = Mobject()
       dummy.add_updater(update_time)
       self.add(dummy)
       self.wait(5)
       dummy.remove_updater(update_time)
       
    
