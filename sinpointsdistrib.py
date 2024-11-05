from manim import *
import numpy as np

class SinPointsDistribution(Scene):
    def construct(self):
        # Titre de la scène
        title_msg = r"\(A = \left\{\sin\left(\dfrac{2n\pi}{7}"
        title_msg += r"\right), n\in\mathbb{Z}\right\}\)"
        title = Title(title_msg)
        self.play(Write(title.scale(0.75)))

        # Création du cercle trigonométrique
        circle = Circle(radius=2, color=WHITE)
        
        # Axes
        axes = Axes(
            x_range=[-2.5, 2.5], y_range=[-2.5, 2.5],
            x_length=5, y_length=5,
            axis_config={"include_tip": True}
        )
        
        # Points dans le sens direct (0 à 6π/7)
        direct_angles = [0, 1, 2, 3]  # Coefficients pour 2π/7
        direct_points = []
        direct_labels = []
        
        for n in direct_angles:
            # Calcul de l'angle et du point
            angle = 2 * n * PI / 7
            x = 2 * np.cos(angle)
            y = 2 * np.sin(angle)
            
            # Point et étiquette
            point = Dot(point=[x, y, 0], color=GREEN)
            if n == 0:
                label = MathTex("0").next_to(point, DOWN)
            else:
                label = MathTex(f"\\dfrac{{{2*n}\\pi}}{{7}}").next_to(point, DOWN)
            
            direct_points.append(point)
            direct_labels.append(label)
        
        # Points dans le sens indirect (-2π/7 à -6π/7)
        indirect_angles = [-1, -2, -3]  # Coefficients pour 2π/7
        indirect_points = []
        indirect_labels = []
        
        for n in indirect_angles:
            angle = 2 * n * PI / 7
            x = 2 * np.cos(angle)
            y = 2 * np.sin(angle)
            
            point = Dot(point=[x, y, 0], color=RED)
            label = MathTex(f"\\dfrac{{{2*n}\\pi}}{{7}}").next_to(point, DOWN)
            
            indirect_points.append(point)
            indirect_labels.append(label)
        
        # Valeurs exactes du sup et inf
        # sin(4π/7) est le maximum et sin(-4π/7) est le minimum
        sup_y = 2 * np.sin(4*PI/7)
        inf_y = 2 * np.sin(-4*PI/7)
        
        sup_line = DashedLine(
            start=[-2.5, sup_y, 0],
            end=[2.5, sup_y, 0],
            color=GREEN
        )
        
        inf_line = DashedLine(
            start=[-2.5, inf_y, 0],
            end=[2.5, inf_y, 0],
            color=RED
        )
        
        # Textes pour sup et inf avec valeurs exactes
        sup_text = MathTex("sup(A) = \\sin\\left(\\dfrac{4\\pi}{7}\\right)").next_to(sup_line, RIGHT)
        inf_text = MathTex("inf(A) = \\sin\\left(-\\dfrac{4\\pi}{7}\\right)").next_to(inf_line, RIGHT)
        
        # Animation
        self.play(Create(axes))
        self.play(Create(circle))
        
        # Affichage des points dans le sens direct avec leurs étiquettes
        for point, label in zip(direct_points, direct_labels):
            self.play(
                Create(point),
                Write(label),
                run_time=1
            )
        
        # Affichage des points dans le sens indirect avec leurs étiquettes
        for point, label in zip(indirect_points, indirect_labels):
            self.play(
                Create(point),
                Write(label),
                run_time=1
            )
        
        # Encadrement des points extrêmes
        sup_dot_box = SurroundingRectangle(direct_points[2])
        inf_dot_box = SurroundingRectangle(indirect_points[1])

        # Affichage des bornes avec leurs valeurs exactes
        self.play(
            Create(sup_line),
            Create(inf_line),
            Write(sup_dot_box),
            Write(inf_dot_box),
            Write(sup_text.scale(0.75)),
            Write(inf_text.scale(0.75))
        )
        
        self.wait(2)

        # Encadrement des textes
        sup_txt_box = SurroundingRectangle(sup_text)
        inf_txt_box = SurroundingRectangle(inf_text) 

        self.play(
            Write(SurroundingRectangle(direct_labels[2])),
            Write(SurroundingRectangle(indirect_labels[1])),
            ReplacementTransform(sup_dot_box, sup_txt_box),
            ReplacementTransform(inf_dot_box, inf_txt_box)      
        )
