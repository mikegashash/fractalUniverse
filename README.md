# fractalUniverse
Simulate a universe in python code simply enough that it can run in browser on google colab. 

Introduction

This project is a Cosmic Fractal Universe Simulation that generates beautiful 3D fractal structures using something called the Mandelbrot Set. Don’t worry if you don’t know what that is! Think of it like a magical way to create colorful, crazy patterns that stretch on forever!

You can control the view of the simulation, change how complex it is, and even zoom in to see different parts of the fractal universe. The simulation is interactive and lets you explore how these patterns grow and evolve in 3D space.

What Does This Code Do?
Imagine you’re making a big drawing on a piece of paper, but instead of just drawing with a pen, you're letting the computer do all the work for you. The computer draws tiny dots in a pattern based on a bunch of rules. These rules help create cool shapes that look like they go on forever—just like stars or galaxies in the universe!

Here’s what the code does:

Generates a Fractal Pattern:

The Mandelbrot Set is a mathematical formula that makes neat patterns. It helps create cosmic shapes that look like they could be part of a faraway universe.
3D Plotting:

The code doesn’t just make a flat picture. It builds a 3D universe where you can see different layers of these patterns, as if they are floating in space!
Add Randomness (Noise):

To make things more fun and less predictable, we add a bit of random noise to make each part of the universe a little different from the rest.

Interactive Controls:

You can move around the universe and zoom in/out on different parts to see the fractals from different angles.
There are sliders to change the azimuth (left/right view), elevation (up/down view), and complexity (how detailed the fractal is).
Key Parts of the Code

Mandelbrot Function:

This part of the code is like a set of instructions that tells the computer how to create the fractal. It checks each dot on the screen and asks, “Does this dot follow the Mandelbrot rule?”
If it follows the rule, it stays. If not, the computer stops and moves on to the next dot.

UniverseSimulation Class:

This is like the “control center” of the universe. It uses the Mandelbrot function to create the universe, then adds depth to make it 3D.
It also controls how the universe looks, using something called a color map to make it pretty.
Sliders:

There are three sliders that let you control how you look at the universe:
Azimuth: Moves your view left or right.
Elevation: Moves your view up or down.
Complexity: Adjusts how detailed or “crazy” the fractals are.

How to Use the Code:

Install the Required Packages:

This is the first step to run the simulation. The code installs everything needed to draw the universe.
Run the Code:

After setting everything up, the code generates a fractal universe based on the Mandelbrot Set.

Interact with Sliders:

Use the sliders to explore the universe:
Move around the 3D universe by changing the azimuth and elevation.
Make the universe more or less detailed by adjusting the complexity slider.

Enjoy the View!:

The code creates a stunning 3D picture of a fractal universe. You can sit back and enjoy the beauty of infinite patterns.
Key Terms Explained

Mandelbrot Set: A special formula that makes shapes look like they repeat over and over, no matter how close you look. It’s a famous example of fractals.

Fractal: A never-ending pattern that looks the same, no matter how much you zoom in. Kind of like a snowflake, but more complicated.

3D Plot: A picture that shows height, width, and depth to make it look like you can fly around the shapes.
