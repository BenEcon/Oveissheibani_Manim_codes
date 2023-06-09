from manim import *
import numpy as np

class FeynmanDiagram(Scene):
    def construct(self):
        self.create_particle_interaction(0, 0, 1, 0,np.radians(45),2)

    def create_particle_interaction(self, x1, y1, x2, y2, angle, l):
        # Convert 2D coordinates to 3D


        # Create arrows for the particles
        particle1 = Line(start=(x1,y1,0), end=(x1-np.sin(angle)*l,y1-np.cos(angle)*l,0)  , color=WHITE)
        particle2 = Line(start=(x1,y1,0), end=(x1-np.sin(angle)*l,y1+np.cos(angle)*l,0) , color=WHITE)
        particle3 = Line(start=(x2,y2,0), end=(x2+np.sin(angle)*l,y2-np.cos(angle)*l,0)  , color=WHITE)
        particle4 = Line(start=(x2,y2,0), end=(x2+np.sin(angle)*l,y2+np.cos(angle)*l,0) , color=WHITE)

        start = np.array([x1, y1, 0])
        end = np.array([x2, y2, 0])
# Number of valleys you want
        n_valleys = 5
        Amp=1
# Create a sinusoidal photon between the particles
        photon = ParametricFunction(
            lambda t: (1-t)*start + t*end + np.sin(2*PI*n_valleys*t)*UP*0.3,
            t_range=np.array([0, 1]),
            color=YELLOW
        )
        self.add(particle1,particle2,photon,particle3,particle4)
        return VGroup(particle1,particle2,photon,particle3,particle4)
