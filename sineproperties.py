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
            
            math_formula = MathTex(formula).to_edge(DOWN)
            self.play(Write(math_formula))

            # Attend un peu
            self.wait(2)

            return point1, point2, line1, line2, math_formula


        def generate_sym(angles, num, den, sym, form):
            for i in range(len(angles)):
                angle = angles[i]
                if i == 0: anglab = r"0"
                else:
                    anglab = r"\frac{" + f"{num[i]}" + r"}{"
                    anglab += f"{den[i]}" + r"}"
                if sym == r"-": 
                    if i == 0: 
                        symangle = 0
                        manglab = anglab
                    else:
                        symangle = -angle
                        manglab = r"-" + anglab
                    if i < 2: p1_pos, p2_pos = RIGHT, RIGHT
                    else: p1_pos, p2_pos = LEFT, LEFT
                elif sym == r"\pi - x": 
                    symangle = PI - angle
                    if i == 0: manglab = r"\pi"
                    else: manglab = r"\pi - " + anglab
                    if i < 2: p1_pos, p2_pos = RIGHT, LEFT
                    else: p1_pos, p2_pos = LEFT, RIGHT
                else: symangle = 0
                p1, p2, l1, l2, formula = show_symmetry(
                    angle, 
                    symangle, 
                    form
                )
                p1_lab = MathTex(anglab).next_to(p1, p1_pos)
                p2_lab = MathTex(manglab).next_to(p2, p2_pos)
                self.play(
                    Write(p1_lab),
                    Write(p2_lab)
                    )
                self.wait(1.5)

                self.play(
                    Uncreate(p1),
                    Uncreate(p2),
                    Uncreate(l1),
                    Uncreate(l2),
                    Unwrite(p1_lab),
                    Unwrite(p2_lab),
                    Unwrite(formula)
                )
                self.wait()


            

        # Phase 1 : Symétrie par rapport à l'axe des abscisses
        angles = [0, 2*PI/7, 4*PI/7, 6*PI/7]
        num = [r"0", r"2\pi", r"4\pi", r"6\pi"]
        den = [7, 7, 7, 7]
        sym = r"-"
        form = r"\sin(-x) = -\sin(x)"
        generate_sym(angles, num, den, sym, form)
        

        # Phase 2 : Symétrie par rapport à la droite d'équation x = 0
        angles = [0, 2*PI/7, 4*PI/7, 6*PI/7]
        num = [r"0", r"2\pi", r"4\pi", r"6\pi"]
        den = [7, 7, 7, 7]
        sym = r"\pi - x"
        form = r"\sin(\pi - x) = \sin(x)"
        generate_sym(angles, num, den, sym, form)
        
        self.wait()
