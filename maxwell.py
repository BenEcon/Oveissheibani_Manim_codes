from manim import *

class MaxwellsEquations(Scene):
    def construct(self):
        # Create equations
        eq1 = MathTex("\\nabla \\cdot \\mathbf{E} = \\frac {\\rho} {\\varepsilon_0}")
        eq2 = MathTex("\\nabla \\cdot \\mathbf{B} = 0")
        eq3 = MathTex("\\nabla \\times \\mathbf{E} = -\\frac {\\partial \\mathbf{B}} {\\partial t}")
        eq4 = MathTex("\\nabla \\times \\mathbf{B} = \\mu_0 \\mathbf{J} + \\mu_0 \\varepsilon_0 \\frac {\\partial \\mathbf{E}} {\\partial t}")
        eq5= MathTex("\\nabla \\cdot \\mathbf{E} = \\frac {\\rho} {\\varepsilon_0}")

        # Create descriptions
        desc1 = Text("Gauss's Law: Electric fields diverge from positive charges").to_edge(DOWN).scale_to_fit_width(self.camera.frame_width - 2)
        desc2 = Text("Gauss's Law for Magnetism: There are no magnetic monopoles").to_edge(DOWN).scale_to_fit_width(self.camera.frame_width - 2)
        desc3 = Text("Faraday's Law: Changing magnetic field creates an electric field").to_edge(DOWN).scale_to_fit_width(self.camera.frame_width - 2)
        desc4 = Text("Ampère's Law with Maxwell's Addition: Magnetic fields circulate around currents and changing electric fields").to_edge(DOWN).scale_to_fit_width(self.camera.frame_width - 2)
        

        # Show first equation and description
        self.play(Write(eq1))
        self.play(Write(desc1))
        self.wait(4)

        # Transform to second equation and description
        self.play(Transform(eq1, eq2), Transform(desc1, desc2))
        self.wait(4)

        # Transform to third equation and description
        self.play(Transform(eq1, eq3), Transform(desc1, desc3))
        self.wait(4)

        # Transform to fourth equation and description
        self.play(Transform(eq1, eq4), Transform(desc1, desc4))
        self.wait(4)

        # Arrange all equations vertically
        equations = VGroup(eq5, eq2, eq3, eq4).arrange(DOWN)
        self.play(Transform(eq1, equations))


class SpeedOfLight(Scene):
    def construct(self):
        # Write down the speed of light equation
        eq = MathTex("c = \\frac {1} {\\sqrt{\\mu_0 \\varepsilon_0}}")
        self.play(Write(eq))
        self.wait(1)

        # Add explanation for epsilon0
        arrow_to_eps = Arrow(start=DOWN, end=eq[0][7].get_center(), buff=0.1, color=BLUE)
        eps_desc = MathTex("\\varepsilon_0", ": \\text{Permittivity of free space}").next_to(arrow_to_eps, DOWN)
        self.play(Create(arrow_to_eps), Write(eps_desc))
        self.wait(1)

        # Add explanation for mu0
        arrow_to_mu = Arrow(start=DOWN*3, end=eq[0][8].get_center(), buff=0.1, color=RED)
        mu_desc = MathTex("\\mu_0", ": \\text{Permeability of free space}").next_to(arrow_to_mu, DOWN)
        self.play(Create(arrow_to_mu), Write(mu_desc))
        self.wait(2)
