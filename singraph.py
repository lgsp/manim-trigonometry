from manim import *

class SinGraph(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-8, 8, 2],
            y_range=[-1.5, 1.5, 0.5],
            x_length=16,
            axis_config={"color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-7.5, 7.5, 2),
                "numbers_with_elongated_ticks": np.arange(-7.5, 7.5, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()
        sin_graph = axes.plot(lambda x: np.sin(2 * x * PI / 7), color=BLUE)
 
        sin_label = axes.get_graph_label(
            sin_graph, r"\sin\left(\dfrac{2x\pi}{7}\right)", x_val=7/4, direction=3 * UP / 4
        )
        
        left_vert_line = axes.get_vertical_line(
            axes.i2gp(-1.75, sin_graph), color=YELLOW, line_func=Line
        )
    
        
        right_vert_line = axes.get_vertical_line(
            axes.c2p(1.75, 2.175), color=YELLOW, line_func=Line
        )

        plot = VGroup(
            axes, 
            sin_graph, 
            left_vert_line, 
            right_vert_line
        )
        labels = VGroup(axes_labels, sin_label)
        self.play(
            Create(plot), 
            Write(labels)
        )
