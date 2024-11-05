from manim import *

class SinusProperties(Scene):
    def construct(self):
        # Cercle trigonométrique
        circle = Circle(radius=2, color=BLUE)
        self.play(Create(circle))

        # Axes
        axes = Axes(
            x_range=[-3.5, 3.5, 1],
            y_range=[-1.2, 1.2, 0.5],
            tips=False
        )
        self.play(Create(axes))

        # Titre
        title = Text(
            "Propriétés de la fonction sinus"
            ).to_edge(UP)
        self.play(Write(title))

        def show_symmetry(angle1, angle2, formula):
            # Crée les points et les rayons
            point1 = Dot(
                radius=0.1, 
                color=RED
                ).move_to(circle.point_at_angle(angle1))
            point2 = Dot(
                radius=0.1, 
                color=RED
                ).move_to(circle.point_at_angle(angle2))
            line1 = Line(ORIGIN, point1, color=GRAY)
            line2 = Line(ORIGIN, point2, color=GRAY)

            # Affiche les points, les rayons et la formule
            self.play(
                Create(point1), 
                Create(point2), 
                Create(line1), 
                Create(line2)
                )
            self.play(Write(MathTex(formula).to_edge(DOWN)))

            # Attend un peu
            self.wait(2)

            return point1, point2, line1, line2


        def generate_sym(angles, num, den, sym, form):
            for i in range(1, len(angles)):
                angle = angles[i]
                anglab = r"\frac{" + f"{num[i]}" + r"}{"
                anglab += f"{den[i]}" + r"}"
                if sym == r"-": 
                    symangle = -angle
                    manglab = r"-" + anglab
                elif sym == r"\pi - x": 
                    symangle = PI - angle
                    manglab = r"\pi - " + anglab
                else: symangle = 0
                p1, p2, l1, l2 = show_symmetry(
                    angle, 
                    symangle, 
                    form
                )
                self.play(
                    Write(MathTex(anglab).next_to(p1, RIGHT)),
                    Write(MathTex(manglab).next_to(p2, RIGHT))
                    )
                self.wait()

            self.play(
                Uncreate(p1),
                Uncreate(p2),
                Uncreate(l1),
                Uncreate(l2)
            )
            self.wait()

        # Phase 1 : Symétrie par rapport à l'axe des abscisses
        angles = [PI/6, PI/4, PI/3]
        num = [r"\pi", r"\pi", r"\pi"]
        den = [6, 4, 3]
        sym = r"-"
        form = r"\sin(-x) = -\sin(x)"
        generate_sym(angles, num, den, sym, form)
        

        # Phase 2 : Symétrie par rapport à la droite d'équation x = 0
        angles = [PI/6, PI/4, PI/3]
        num = [r"\pi", r"\pi", r"\pi"]
        den = [6, 4, 3]
        sym = r"\pi - x"
        form = r"\sin(\pi - x) = \sin(x)"
        generate_sym(angles, num, den, sym, form)
        
        self.wait()
