from manim import *

class ExampleScene(Scene):
    def construct(self):
        # Define the function f(x, y, z)
        def f(x, y):
            z = x**2 + y**2
            return z

        # Define the x and y ranges
        x_range = [-3, 3]
        y_range = [-3, 3]

        # Create the Surface with custom color mapping
        surface = Surface(
            lambda x, y: [x, y, f(x, y)],
            v_range=x_range,
            u_range=y_range,
            fill_opacity=1,
            resolution=(50, 50),
        )

        # Apply custom color mapping based on z value
        surface.set_color_by_vertex(lambda p: interpolate_color(RED, BLUE, normalize(p.z_value)))

        self.add(surface)
        self.wait()
