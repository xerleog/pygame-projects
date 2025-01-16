# Galaxy Simulation

## Description

This project simulates a night-time galaxy view with twinkling stars. The `main.py` script generates stars of varying colors and sizes. The stars will twinkle by continuously adding new stars and changing the radii of existing ones, creating a dynamic and visually engaging effect.

## Features

- **Dynamic Star Generation**: New stars are generated with random colors, positions, and sizes.
- **Twinkling Effect**: A queue is used to cycle stars, replacing the oldest ones while adjusting their sizes for a twinkling effect.
- **Real-Time Simulation**: The galaxy simulates in real-time, showing the continuous appearance and twinkling of stars.

The simulation will start, displaying the galaxy where the stars twinkle in real-time.
## Algorithm 

The core of the simulation is based on the concept of twinkling stars, and the algorithm works as follows:
1. **Dynamic Star Generation**: A new star is added to the screen every cycle. Each star has a random position, color, and radius.
2. **Twinkling Effect**: A queue is used to create a cycle where the first star is removed and replaced with a new one. The radius of the stars is calculated based on a random value to create the twinkling effect.
3. **Radius Calculation**: The radius is calculated as a floating-point value between a specified minimum and maximum range to give the stars a varied and dynamic appearance.
