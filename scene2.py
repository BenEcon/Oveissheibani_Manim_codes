from manim import *
from manim_physics import *
import numpy as np
from manim import config
import random




class part3(ThreeDScene):
    def construct(self):




        self.t_offset = 0
        axes = ThreeDAxes(x_range=(-2, 2, 1), y_range=(-2, 2, 1), z_range=(-2, +2, 1)).shift(RIGHT*3)
        axes1 = ThreeDAxes(x_range=(-2, 2, 1), y_range=(-2, 2, 1), z_range=(-2, +2, 1)).shift(LEFT*3)
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)


 
 

        # Add the axes and labels to the scene
        #self.add(axes, x_label, y_label, z_label)
        dummy = Mobject()
        orange_color = rgb_to_color([255/255, 165/255, 0])
        
        

        def update_time(mob,dt):
            self.t_offset += dt


        def em_electric_field(point: np.array,A,freq) -> np.array:
             x, y, z = point
             return np.array([0, A   *  np.sin(freq*(x-self.t_offset)), 0])

        def em_magnetic_field(point: np.array,A,freq) -> np.array:
            x, y, z = point
            return np.array([0, 0, A * np.cos(freq*(x-self.t_offset))])


        def em_electric_field1(point: np.array,A,freq) -> np.array:
             x, y, z = point
             return np.array([0, A   *  np.sin(freq*(x-self.t_offset)), A   *  np.cos(freq*(x+self.t_offset))])

        def em_magnetic_field1(point: np.array,A,freq) -> np.array:
            x, y, z = point
            return np.array([0, A * np.sin(freq*(x+self.t_offset)), A * np.cos(freq*(x-self.t_offset)) ])

 
        def oscillation_function(A,freq):
            return np.array([0,0, A* np.sin(freq*self.t_offset)])
            
        def oscillation_function1(A,freq):
            return np.array([0,A* np.cos(freq*self.t_offset), A* np.sin(freq*self.t_offset)])

        #self.play(ApplyFunction(oscillation_function, sphere), run_time=5, rate_func=linear)
        sphere1 = always_redraw(lambda: Sphere(radius=0.09, center=oscillation_function(1,5),fill_opacity=0.9).set_color(RED).shift(RIGHT*3).scale(0.8))
        sphere = always_redraw(lambda: Sphere(radius=0.09, center=oscillation_function(1,20),fill_opacity=0.9).set_color(RED).shift(LEFT*3).scale(0.8))

        E_field = always_redraw(lambda :ArrowVectorField(lambda p: em_electric_field(p, 2, 10), color=rgb_to_color([138/255,43/255,226/255]), x_range=[-2,2, 0.05], y_range=[-0, 0, 1], z_range=[-0, 0, 1]).shift(RIGHT*3))
        B_field = always_redraw(lambda :ArrowVectorField(lambda p: em_magnetic_field(p, 2, 10), color=PURPLE, x_range=[-2, 2, 0.05], y_range=[-0, 0, 1], z_range=[-0, 0, 1]).shift(RIGHT*3))


        E_field1 = always_redraw(lambda :ArrowVectorField(lambda p: em_electric_field(p, 2, 5), color=GREEN, x_range=[-2,2, 0.05], y_range=[-0, 0, 1], z_range=[-0, 0, 1]).shift(LEFT*3))
        B_field1 = always_redraw(lambda :ArrowVectorField(lambda p: em_magnetic_field(p, 2, 5), color=GREEN_C, x_range=[-2, 2, 0.05], y_range=[-0, 0, 1], z_range=[-0, 0, 1]).shift(LEFT*3))


        self.add( E_field, B_field,sphere, E_field1, B_field1,sphere1)
        
        
        
#
#
#        self.begin_ambient_camera_rotation(rate=0.4)
        dummy.add_updater(update_time)
        self.add(dummy)
        self.wait(10)
        dummy.remove_updater(update_time)



#
