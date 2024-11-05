from manim import *

class ExplainSetA(Scene):
    def construct(self):
        # Titre
        title = Title("Cherchons les extrema de l'ensemble A")
        self.play(Write(title.scale(0.7)))

        # Définition de A
        a_def = r"\(A = \{ \sin\left(\frac{2n\pi}{7}\right) "
        a_def += r"\mid n \in \mathbb{Z}\}\)"
        definition = Tex(a_def)
        self.play(Write(definition.scale(0.7).next_to(title, DOWN)))

        # Périodicité
        period = r"La fonction sinus est $2\pi$-périodique."
        periodicity = Tex(period)
        self.play(Write(periodicity.scale(0.7).next_to(definition, DOWN)))

        # Réduction à un ensemble fini
        fini = r"On peut se ramener à étudier $n$ dans "
        fini += r"$\{0, 1, 2, 3, 4, 5, 6\}$"
        finite_set = Tex(fini)
        self.play(Write(finite_set.scale(0.7).next_to(periodicity, DOWN)))

        # Valeurs exact

        # Angles correspondants
        angl = r"Angles correspondants : "
        angl += r"\(0, \frac{2\pi}{7}, \frac{4\pi}{7}, "
        angl += r"\frac{6\pi}{7}, \frac{8\pi}{7},"
        angl += r" \frac{10\pi}{7}, \frac{12\pi}{7}\)"
        angles = Tex(angl)
        self.play(Write(angles.scale(0.7).next_to(finite_set, DOWN)))

        self.wait()

        # Créer un cercle trigonométrique
        circle = Circle(radius=2, color=BLUE).next_to(angles, DOWN)
        self.play(Create(circle))

        # Points d'angle 0 et pi
        point_0 = Dot(color=GREEN).move_to(circle.point_at_angle(0))
        point_pi = Dot(color=GREEN).move_to(circle.point_at_angle(PI))
        #self.play(Create(point_0), Create(point_pi))

        # Calcul du centre (milieu de [point_0, point_pi])
        center = (point_0.get_center() + point_pi.get_center()) / 2

        self.wait() 

        # Ajouter les points sur le cercle
        points = VGroup()
        for n in range(7):
            angle = 2*n*PI/7
            point = Dot(color=RED).move_to(circle.point_at_angle(angle))
            ray = Line(center, point, color=GRAY)
            if n == 0: lab = r"\(0\)"
            else: lab = r"\(\frac{" + f"{2*n}" + r"}{7}\pi\)"
            angle_label = Tex(lab).next_to(point, RIGHT, buff=0.2)  # Valeur exacte de l'angle

            points.add(point)
            self.play(Create(ray), Create(point), Write(angle_label))

        self.wait()
