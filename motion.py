from manim import *
import numpy as np

class CircularMotion(Scene):
    def construct(self):

        self.t_offset = 0
        dummy = Mobject()
        text=Text("Apply particle-wave to describe the motion of electron around the nuclei",width=self.camera.frame_width *0.9).shift(UP*2).scale(0.7)
        #self.play(Write(text))
        path_center = ORIGIN


        def oscillation_function(A,freq):
            return np.array([(A-self.t_offset*0.1)*np.cos(freq*self.t_offset),(A-self.t_offset*0.1)*np.sin(freq*self.t_offset), 0])


        sphere = always_redraw(lambda: Sphere(radius=0.07, center=oscillation_function(2,10),fill_opacity=0.9).set_color(BLUE))


#
#                       lambda t: (1-t)*sphere.get_center() + np.sin(2*PI*t)*UP*0.3,
#                t_range=np.array([0, 1]),




        nuc=Sphere(radius=0.2, center=ORIGIN,fill_opacity=0.9).set_color(RED)
        def update_time(mob,dt):
            self.t_offset += dt

        self.add(dummy,sphere,nuc)
        dummy.add_updater(update_time)
        self.play(sphere.animate,nuc.animate)
        self.wait(20)
        dummy.remove_updater(update_time)



##
#
#from manim import *
#import numpy as np
#
#class CircularMotion(Scene):
#    def construct(self):
#        self.t_offset = 0
#        dummy = Mobject()
#        text = Text("Apply particle-wave to describe the motion of electron around the nuclei", width=self.camera.frame_width *0.9).shift(UP*2).scale(0.7)
#        path_center = ORIGIN
#
#        def oscillation_function(A, freq):
#            return np.array([(A - self.t_offset*0.1)*np.cos(freq*self.t_offset), (A - self.t_offset*0.1)*np.sin(freq*self.t_offset), 0])
#
#        sphere = always_redraw(lambda: Sphere(radius=0.09, center=oscillation_function(2,10), fill_opacity=0.9).set_color(BLUE))
#
#        nuc = Sphere(radius=0.2, center=ORIGIN, fill_opacity=0.9).set_color(RED)
#
#        # Create a trajectory using a VMobject
#        trajectory = VMobject()
#
#        # reshape before passing to set_points_as_corners
#        sphere_center_reshaped = sphere.get_center().reshape(1, 3)
#        trajectory.set_points_as_corners([*sphere_center_reshaped])
#
#        def update_trajectory(traj, sphere):
#            # Reshape the sphere center to match the trajectory points
#            sphere_center_reshaped = sphere.get_center().reshape(1, 3)
#            new_points = [*traj.get_points(), *sphere_center_reshaped]
#            traj.set_points_as_corners(new_points)
#
#        trajectory.add_updater(lambda m: update_trajectory(m, sphere))
#
#        def update_time(mob, dt):
#            self.t_offset += dt
#
#        self.add(dummy, sphere, nuc, trajectory)
#        dummy.add_updater(update_time)
#        self.play(sphere.animate, nuc.animate)
#        self.wait(3)
#        dummy.remove_updater(update_time)
