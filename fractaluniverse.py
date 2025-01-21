# Install required packages for Google Colab
!pip install numpy matplotlib ipywidgets numba plotly
from google.colab import output
output.enable_custom_widget_manager()  # Enable custom widgets in Colab

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output
import plotly.graph_objects as go
from numba import njit, prange

# Generate a 3D galaxy-like distribution with age-based colors
@njit(parallel=True)
def generate_galaxy(num_stars, spread, spiral_arms, rotation):
    theta = np.linspace(0, 2 * np.pi * spiral_arms, num_stars)
    r = spread * np.sqrt(np.random.rand(num_stars))
    x = r * np.cos(theta + rotation * r)
    y = r * np.sin(theta + rotation * r)
    z = spread * (np.random.rand(num_stars) - 0.5)
    age = np.random.rand(num_stars)  # Age factor for color coding
    velocity = np.random.rand(num_stars, 3) - 0.5  # Random initial velocities
    return x, y, z, age, velocity

# Universe simulation class
class GalacticSimulation:
    def __init__(self, num_stars=10000, spread=50, spiral_arms=2, rotation=2.0):
        self.num_stars = num_stars
        self.spread = spread
        self.spiral_arms = spiral_arms
        self.rotation = rotation
        self.velocities = None
        self.fig = go.Figure()
        self.update_galaxy()

    def update_galaxy(self):
        x, y, z, age, velocity = generate_galaxy(self.num_stars, self.spread, self.spiral_arms, self.rotation)
        self.velocities = velocity
        self.fig.data = []
        self.fig.add_trace(go.Scatter3d(
            x=x, y=y, z=z,
            mode='markers',
            marker=dict(
                size=1.5,
                color=age,  # Star colors based on age
                colorscale='YlOrRd',
                opacity=0.8
            )
        ))
        self.fig.update_layout(
            scene=dict(
                xaxis=dict(title='X', showgrid=False),
                yaxis=dict(title='Y', showgrid=False),
                zaxis=dict(title='Z', showgrid=False),
                aspectmode='cube',
                camera=dict(
                    eye=dict(x=1.5, y=1.5, z=1.0)
                )
            ),
            title="3D Galactic Spiral with Nebula Effects",
            height=700,
            width=900,
            template='plotly_dark'
        )

    def animate_galaxy(self, steps=100):
        for _ in range(steps):
            self.fig.update_layout(scene_camera=dict(eye=dict(x=np.cos(_ / 20) * 1.5, 
                                                             y=np.sin(_ / 20) * 1.5, 
                                                             z=1.0)))
            self.fig.show()

    def update_parameters(self, spread, spiral_arms, rotation):
        self.spread = spread
        self.spiral_arms = spiral_arms
        self.rotation = rotation
        self.update_galaxy()

# Create galaxy simulation instance
sim = GalacticSimulation()

# Create sliders
spread_slider = widgets.FloatSlider(value=50, min=10, max=100, step=1, description='Spread')
spiral_slider = widgets.FloatSlider(value=2, min=1, max=5, step=0.1, description='Spiral Arms')
rotation_slider = widgets.FloatSlider(value=2.0, min=0.1, max=5.0, step=0.1, description='Rotation')

# Update function
def update_plot(change):
    clear_output(wait=True)
    display(widgets.VBox([spread_slider, spiral_slider, rotation_slider]))
    sim.update_parameters(spread_slider.value, spiral_slider.value, rotation_slider.value)
    sim.fig.show()

# Link sliders to update function
spread_slider.observe(update_plot, names='value')
spiral_slider.observe(update_plot, names='value')
rotation_slider.observe(update_plot, names='value')

# Display UI
display(widgets.VBox([spread_slider, spiral_slider, rotation_slider]))
sim.fig.show()
