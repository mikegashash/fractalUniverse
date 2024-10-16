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
from matplotlib.colors import LinearSegmentedColormap
from numba import njit, prange

# Optimized Mandelbrot computation using Numba with parallel loops
@njit(parallel=True)
def mandelbrot(h, w, max_iter, center, zoom):
    # Define the x and y grid ranges
    x = np.linspace(-1.5 / zoom, 0.5 / zoom, w)
    y = np.linspace(1 / zoom, -1 / zoom, h)

    # Ensure shape compatibility for broadcasting by reshaping arrays
    x = x.reshape(1, -1)  # Shape (1, w)
    y = y.reshape(-1, 1)  # Shape (h, 1)

    # Create the complex grid for Mandelbrot
    c = x + y * 1j + complex(*center)
    z = np.zeros_like(c)
    divtime = np.zeros(c.shape, dtype=np.int32)  # To store divergence times

    # Mandelbrot iteration with manual loop
    for i in prange(h):
        for j in range(w):
            for k in range(max_iter):
                z[i, j] = z[i, j]**2 + c[i, j]
                if abs(z[i, j]) > 2:
                    divtime[i, j] = k  # Record the iteration where divergence happens
                    break
    return divtime  # Return the divergence times

# Custom colormap for better visuals
def create_custom_cmap():
    colors = ['#000000', '#1B1734', '#3B4178', '#5A6DBE', '#7A9BFF', '#9AC9FF',
              '#BBEBF7', '#CCF2E9', '#FFFFFF']
    return LinearSegmentedColormap.from_list('custom', colors, N=len(colors))

# Main simulation class
class UniverseSimulation:
    def __init__(self, resolution=100, depth=10, max_iter=50):
        self.resolution = resolution
        self.depth = depth
        self.max_iter = max_iter
        self.center = (-0.5, 0)
        self.zoom = 1
        self.complexity = 0.1
        self.cmap = create_custom_cmap()
        self.fig = go.Figure()  # Use Figure instead of FigureWidget for Colab
        self.update_universe()

    def update_universe(self):
        # Generate the base universe with Mandelbrot
        base_universe = mandelbrot(self.resolution, self.resolution, self.max_iter, self.center, self.zoom)
        base_universe = (base_universe - base_universe.min()) / (base_universe.max() - base_universe.min())
        noise_layer = np.random.random((self.resolution, self.resolution, self.depth))
        depth_factors = np.exp(-np.arange(self.depth) * 0.5).reshape(1, 1, -1)
        self.universe = depth_factors * base_universe[:, :, np.newaxis] + noise_layer * self.depth * self.complexity

    def plot_universe(self, azimuth, elevation):
        if self.universe is None:
            print("No universe to plot.")
            return

        # Create the 3D meshgrid for plotting
        x, y, z = np.meshgrid(range(self.resolution), range(self.resolution), range(self.depth))
        points = np.column_stack((x.ravel(), y.ravel(), z.ravel()))
        values = self.universe.ravel()

        # Update the 3D scatter plot
        self.fig.data = []  # Clear previous data
        self.fig.add_trace(go.Scatter3d(
            x=points[:, 0], y=points[:, 1], z=points[:, 2],
            mode='markers',
            marker=dict(
                size=2,
                color=values,
                colorscale='Viridis',
                opacity=0.8
            )
        ))

        self.fig.update_layout(
            scene=dict(
                xaxis=dict(title='X', showgrid=False),
                yaxis=dict(title='Y', showgrid=False),
                zaxis=dict(title='Z (Depth)', showgrid=False),
                aspectmode='cube',
                camera=dict(
                    eye=dict(
                        x=np.cos(np.radians(azimuth)) * np.cos(np.radians(elevation)),
                        y=np.sin(np.radians(azimuth)) * np.cos(np.radians(elevation)),
                        z=np.sin(np.radians(elevation))
                    )
                )
            ),
            title="Cosmic Fractal Universe",
            height=600,
            width=800
        )

    def update_plot(self, azimuth, elevation, complexity):
        self.complexity = complexity
        self.update_universe()
        self.plot_universe(azimuth, elevation)

# Create the simulation
sim = UniverseSimulation()

# Create sliders for user interaction
azimuth_slider = widgets.FloatSlider(value=0, min=0, max=360, step=1, description='Azimuth')
elevation_slider = widgets.FloatSlider(value=30, min=0, max=90, step=1, description='Elevation')
complexity_slider = widgets.FloatSlider(value=0.1, min=0.01, max=1, step=0.01, description='Complexity')

# Create update function
def update_plot(change):
    clear_output(wait=True)  # Clear previous output
    display(widgets.VBox([azimuth_slider, elevation_slider, complexity_slider]))  # Redisplay sliders
    sim.update_plot(azimuth_slider.value, elevation_slider.value, complexity_slider.value)
    sim.fig.show()  # Explicitly show the updated figure

# Link sliders to the update function
azimuth_slider.observe(update_plot, names='value')
elevation_slider.observe(update_plot, names='value')
complexity_slider.observe(update_plot, names='value')

# Display the sliders and the initial plot
display(widgets.VBox([azimuth_slider, elevation_slider, complexity_slider]))
sim.plot_universe(0, 30)
sim.fig.show()  # Use .show() for Plotly figure in Colab
