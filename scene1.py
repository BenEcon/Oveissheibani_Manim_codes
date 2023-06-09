from manim import *
from manim_physics import *
import numpy as np
from manim import config
import random



class part0(ThreeDScene):
    def construct(self):
        # Create an empty circle
        #self.set_camera_orientation(phi=75 * DEGREES, theta=-160 * DEGREES)
        tex= Text("How has the concept of particle-wave duality fostered a more comprehensive understanding?",t2c={'Duality':RED},width=self.camera.frame_width*0.9)
        self.add(tex.scale(0.8).shift(UP*3))
        self.play(Write(tex))
        self.wait(5)
#        self.play(FadeOut(tex))
        screen_height = self.camera.frame_height
        line = Line(start=UP * (screen_height / 4), end=DOWN * (screen_height / 4), color=WHITE)
        self.add(line)
        self.play(FadeIn(line))
        self.wait(5)
        cir=Circle(radius=1)
        cir.set_fill(color=[PURPLE, YELLOW], opacity=1)
        self.t_offset = 0
        def cos_func(t,A):
            return np.sin((t+self.t_offset)*A)

        wave= always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,A=2),x_range=(-2,+2), color=PURPLE).shift(RIGHT*4))
        wave2=always_redraw(lambda: FunctionGraph(lambda t: cos_func(t,A=4),x_range=(-2,+2), color=YELLOW).shift(RIGHT*4))
        group= Group(wave,wave2)
        self.add(group)

        self.add(wave,cir.shift(LEFT*4))
        def update_time(mob,dt):
            self.t_offset += dt
        dummy = Mobject()
        dummy.add_updater(update_time)
        self.add(dummy)
        self.wait(10)
        tex1= Text("Localized").shift(LEFT*4+DOWN*2)
        tex2= Text("Extended").shift(RIGHT*4+DOWN*2)
        self.play(FadeIn(tex1),FadeIn(tex2))
        self.wait(10)
        dummy.remove_updater(update_time)


class part1(ThreeDScene):
    def construct(self):



         text=[]
         w=self.camera.frame_width *0.8
         text.append(Text("A rigid body behaves similar to a zero dimensional point",t2c={'zero' :RED}, width =w).shift(UP*3))



         equations = [

            MathTex(r"\vec{F}_{\text{total}} = M \vec{A}_{\text{cm}}"),
            MathTex(r"\vec{F}_i = m_i \vec{a}_i"),
            MathTex(r"\sum_{i} \vec{F}_i = \sum_{i} m_i \vec{a}_i"),
         ]


         equations1 = [
            MathTex(r"R_{\text{cm}} = \frac{\sum_{i} m_i \vec{r_i}}{\sum_{i} m_i}",color=RED)
         ]




         self.play(Write(text[0]))
         self.wait(5)


         def compute_center_of_mass(vertices):
            x_coordinates = [vertex[0] for vertex in vertices]
            y_coordinates = [vertex[1] for vertex in vertices]
            z_coordinates = [vertex[2] for vertex in vertices]
            center_of_mass = [sum(x_coordinates) / len(vertices), sum(y_coordinates) / len(vertices), sum(z_coordinates)/ len(vertices)]
            return center_of_mass


        

         points_sets = [
            [[-3, 0, 0], [-4, 1, 0], [-4, -1, 0]],   # 3-sided polygon (triangle) on the left side of the screen

            [[3, 1, 0], [4, 2, 0], [5, 1, 0], [5, -1, 0], [4, -2, 0], [3, -1, 0]],   # 6-sided irregular polygon on the right side of the screen
         ]
         polygons = []
         polygons2=[]
         dots = []
         textondots=[]
         color=[BLUE,RED,YELLOW,GREEN]
         i=0
         for points in points_sets:
            polygon = Polygon(*points, color=color[i%4],fill_opacity=0.8).shift(DOWN)
            polygons.append(polygon)
            self.play(Create(polygon))
            i=i+1

         i=0
         for polygon in polygons:
            center_of_mass = compute_center_of_mass(polygon.get_vertices())
            center_dot = Dot(center_of_mass, color=color[i%4])
            dots.append(center_dot)
            textondot=Text("center of mass").scale(center_dot.radius*8).next_to(center_dot, UP*0.8)
            textondots.append(textondot)
            i=i+1

         i=0


         for polygon, dot in zip(polygons, dots):
            self.play(Transform(polygon, dot))
            self.add(dot)
            self.play(Write(textondots[i]))
            i=i+1

         dot_poly_group = VGroup(*dots)
         #self.play(dot_poly_group.animate.shift(UP*2))
         self.wait(10)
         eq_group = VGroup(*equations).arrange(DOWN)
         eq_group.scale(0.8).to_edge(LEFT*3, buff=1).shift(LEFT*2)
         #self.play(Write(eq_group))
         equations1[0].next_to(equations[1], RIGHT*1.5).scale(0.8)
         #self.play(Write(equations1[0]))




class part2(ThreeDScene):
    def construct(self):


         text=[]
         w=self.camera.frame_width *0.8
         text.append(Text("Electric field is the extension of electric charge into space ",t2c={'zero' :RED}, width =w).shift(UP*3))
         for i in range(len(text)):
            self.play(Write(text[i]))
            self.wait(4)



         self.remove(*text)
         charges = []
         fields = []
         
         n = 2
         self.clear()
         charge1 = Charge(6, LEFT)
         charge2 = Charge(-6, RIGHT)
         field=ElectricField(charge1,charge2)
         self.play(Create(charge1),Create(charge2))
         self.wait(4)
         self.play(Create(field))
         self.wait(6)
         self.remove(field,charge1,charge2)
        

         # Number of charges
         n = 10

         # Radius of the circle on which charges sit
         r = 2
         field = ElectricField()
         # Create the charges
         for i in range(n):
            # Angle for each charge (in radians)
            theta = 2 * np.pi * i / n

            # Position of the charge
            pos = r * np.array([np.cos(theta), np.sin(theta), 0])
            # Create the charge and add it to the charges list
            if (i%2==0):
                charge = Charge(1, pos)
            else:
                charge = Charge(-1, pos)
            charges.append(charge)
            new_field = ElectricField(*charges)
            self.play(Create(charge), Transform(field, new_field))
            fild=new_field
            self.wait(1)
        # Create the electric field
         self.wait(15)
         self.remove(*field,*charge)








class part3(ThreeDScene):
    def construct(self):




        self.t_offset = 0
        axes = ThreeDAxes(x_range=(-2, 2, 1), y_range=(-2, 2, 1), z_range=(-2, +2, 1))
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)



        self.add(axes)
        # Color the axes
        axes.x_axis.set_color(RED)
        axes.y_axis.set_color(GREEN)
        axes.z_axis.set_color(BLUE)
        
        self.wait(3)
        self.play(
            ApplyMethod(axes.x_axis.set_color, WHITE),
            ApplyMethod(axes.y_axis.set_color, WHITE),
            ApplyMethod(axes.z_axis.set_color, WHITE),
        )
        self.wait(3)
        

        # Label the axes
        x_label = Text("X").next_to(axes.x_axis, RIGHT)
        y_label = Text("Y").next_to(axes.y_axis, RIGHT)
        z_label = Text("Z").next_to(axes.z_axis, UP)
        x_label.set_color(axes.x_axis.get_color())
        y_label.set_color(axes.y_axis.get_color())
        z_label.set_color(axes.z_axis.get_color())
        #self.add_fixed_in_frame_mobjects(x_label, y_label, z_label)
        

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
        sphere = always_redraw(lambda: Sphere(radius=0.09, center=oscillation_function(2,5),fill_opacity=0.9).set_color(RED))
        sphere1 = always_redraw(lambda: Sphere(radius=0.09, center=oscillation_function1(2,5),fill_opacity=0.9).set_color(RED))

        E_field = always_redraw(lambda :ArrowVectorField(lambda p: em_electric_field(p, 2, 5), color=BLUE, x_range=[-5,5, 0.05], y_range=[-0, 0, 1], z_range=[-0, 0, 1]))
        B_field = always_redraw(lambda :ArrowVectorField(lambda p: em_magnetic_field(p, 2, 5), color=orange_color, x_range=[-5, 5, 0.1], y_range=[-0, 0, 1], z_range=[-0, 0, 1]))
        self.add(axes, E_field, B_field)

        E_field1 = always_redraw(lambda :ArrowVectorField(lambda p: em_electric_field1(p, 2, 5), color=BLUE, x_range=[-5,5, 0.1], y_range=[-0, 0, 1], z_range=[-0, 0, 1]))
        B_field1 = always_redraw(lambda :ArrowVectorField(lambda p: em_magnetic_field1(p, 2, 5), color=orange_color, x_range=[-5, 5, 0.1], y_range=[-0, 0, 1], z_range=[-0, 0, 1]))


        self.add(axes, E_field, B_field,sphere)
        self.begin_ambient_camera_rotation(rate=0.4)
        dummy.add_updater(update_time)
        self.add(dummy)
        self.wait(25)
        self.remove(E_field,B_field,sphere)
        self.wait(3)
        self.add(E_field1,B_field1,sphere1)
        self.wait(25)
        dummy.remove_updater(update_time)



#
#
class Part4(ThreeDScene):
    def construct(self):



        self.t_offset = 0


        def cos_func(u, v):
            x = u
            y = v
            sigma_x = 1  # Adjust the value of sigma_x as needed
            sigma_y= 1  # Adjust the value of sigma_x as needed
            A=2
            x0=0
            y0=0
            z = A * np.exp(-(x - self.t_offset)**2 / (2 * sigma_x**2)) * np.exp(-(y - y0)**2 / (2 * sigma_y**2))
            return np.array([x, y, z])




        graph = always_redraw(
            lambda: Surface(
                cos_func,
                resolution=(41, 41),
                color=PURPLE,
                u_range=[0, 1],
                v_range=[0, 1],
            ).shift(self.t_offset * LEFT)
           )
        graph = always_redraw(lambda: FunctionGraph(cos_func, color=PURPLE, x_range=[-3, 3]).shift(self.t_offset * LEFT))

        self.add(graph)



        frame_counter = 0
        update_interval = 10


        axes = ThreeDAxes(x_range=(-2, 2, 0.1), y_range=(-2, 2, 0.1), z_range=(-2, 10, 0.1))

        dummy = Mobject()


        surf=always_redraw(lambda: Surface(cos_func, color=PURPLE,u_range=[-2, 2], v_range=[-2, 2], fill_color=RED))

        def update_time(mob,dt):
            global frame_counter
            frame_counter += 1
            if frame_counter % update_interval == 0:
                self.t_offset += dt



        surf.set_fill_by_value(axes=axes, colorscale=[(RED, 0), (YELLOW, 0.02), (GREEN, 0.5)], axis=2)
        self.add(surf)
        self.play(FadeIn(surf))
   #     self.play(
    #        surf.animate.rotate(90 * DEGREES, axis=Y_AXIS),
     #       surf.animate.rotate(90 * DEGREES, axis=X_AXIS),
      #      surf.shift(RIGHT),
#)
        self.wait(1)



        dummy.add_updater(update_time)
        self.add(dummy)
        self.wait(5)
        graph.animate.shift(LEFT)
        dummy.remove_updater(update_time)





        self.add(cos_func)
        self.play(FadeIn(cos_func))
        self.wait(4)
        self.play(cos_func.animate.scale())


        self.play(FadeIn(tex))
        self.wait(1)
        self.play(FadeOut(tex))
        self.play(Create(circle))
        self.play(Create(line))


        self.wait(3)

