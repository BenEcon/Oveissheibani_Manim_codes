from manim import *
from manim_physics import *
import numpy as np
from manim import config
import random




class equation(ThreeDScene):
    def construct(self):
        
        
        time=10
        fontsize=25
        equation = MathTex(
            r"E_{total}=H_1(x_1)+H_2(x_2)+...",
            substrings_to_isolate="x",
            font_size=40).set_color_by_tex("x", YELLOW)
        self.play(Write(equation))
        self.wait(time)
        self.play(equation.animate.shift(UP*3+LEFT*2))
        

        equation1 = MathTex(
            r"z(x)=\int_{-\infty}^{\infty} \exp \left(\frac{-H(x)}{k T}\right) d x=\int_{-\infty}^{\infty} \exp \left(\frac{-c x^2}{k T}\right) d x=\left(\frac{\pi k T}{c}\right)^{1 / 2}",
        font_size=fontsize)
        self.play(Write(equation1))
        self.wait(time)
        self.play(equation1.animate.shift(UP*2+LEFT*2))

        equation2 = MathTex(
            r"x\rightarrow E_0\; \text{Amplitude}",
        font_size=fontsize).set_color(RED)
        self.play(Write(equation2))
        self.wait(time)
        self.play(equation2.animate.shift(UP*2+RIGHT*4))
        
        equation25 = MathTex(
            r"z(E_0)=\int_{-\infty}^{\infty} \exp \left(\frac{-H(E_0)}{k T}\right) dE_0=\int_{-\infty}^{\infty} \exp \left(\frac{-c E_0^2}{k T}\right) dE_0=\left(\frac{\pi k T}{c}\right)^{1 / 2}",
            font_size=fontsize)


        self.play(Write(equation25))
        self.wait(time)
        self.play(equation25.animate.shift(UP+LEFT*2))
        
        equation4 = MathTex(
            r"H \propto c E_0^2 sin(2 \pi \nu t)",
        font_size=fontsize)
        self.play(Write(equation4))
        self.wait(time)
        self.play(equation4.animate.shift(UP*0+LEFT*4))
        
        equation5 = MathTex(
            r"\bar{H_{\nu}}= \frac{1}{T} \int c E^2(x,t)dt =c/2E_0^2",
        font_size=fontsize)
      
        self.play(Write(equation5))
        self.wait(time)
        self.play(equation5.animate.shift(UP*0+RIGHT*2))
    

  

        equation6= MathTex(
            r"U=k T^2 \frac{d(\ln z)}{d T}=1/2 KT",
        font_size=fontsize).shift(UP*-1)
        self.play(Write(equation6))
        self.wait(time)


        math1=MathTex(r"u(\nu)=\frac{8 \pi \nu^2}{c^3} \bar{H_v} ",font_size=fontsize).shift(UP*(-2)+LEFT)
        math2=MathTex(r"= \frac{8 \pi \nu^2 k T}{c^3}",font_size=fontsize,color=RED).shift(UP*(-2)+RIGHT*0.6)
        self.play(Write(math1),Write(math2))
        self.wait(time)
