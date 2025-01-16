# Ant Simulation 

## Description 

This simulation tool demonstrates the pathfinding behavior of ants in search of food sources. The project contains two main scripts, `main.py` and `main2.py`:

- **`main.py`**: Generates 10 random food sources and simulates the ant's movement from start to finish using brute force to find the shortest path.
- **`main2.py`**: Allows the user to interactively select 10 food source points on the screen. The ant's movements are observed, and its pathfinding behavior is also calculated using brute force.

Both scripts are based on the idea of calculating the shortest possible path to undiscovered food nodes in a simulated environment.

## Features 

- **Random Food Generation**: Generate random food source points on the screen .
- **Interactive Mode**: Let the user select food sources by right-clicking on the screen .
- **Brute Force Pathfinding**: Ants calculate the shortest path to undiscovered food sources using brute force .
- **Real-time Observations**: Track the ant's movements in real-time as it navigates to food sources .

## Installation 

1. Clone this repository to your local machine using `git clone`:

   ```bash
   git clone https://github.com/xerleog/pygame-projects.git
   ```

2. Navigate to the Ant-Simulation project directory:

   ```bash
   cd pygame-projects/Ant-Simulation
   ```

3. Install the required dependencies. If you're using `pip`, install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

   Otherwise, ensure you have `pygame` and other necessary libraries installed manually.

## Usage

### Running `main.py`

1. This script generates 10 random food source points and simulates the ant’s pathfinding behavior using brute force to calculate the shortest path.

   To run `main.py`:

   ```bash
   python3 main.py
   ```

   The simulation will start with 10 randomly generated food sources, and the ant will calculate and follow the shortest paths between them.

### Running `main2.py`

2. This script allows the user to select food source points on the screen by right-clicking. Once 10 points are selected, the simulation will begin, and the ant will calculate the shortest paths to reach the food sources.

   To run `main2.py`:

   ```bash
   python3 main2.py
   ```

   After running, right-click on the screen to select food points (10 points). The ant will calculate the shortest paths to reach each food source.

## Algorithm 

Both `main.py` and `main2.py` use brute force to calculate the shortest path to undiscovered food nodes. The brute-force method involves:

1. Considering all possible paths the ant can take.
2. Calculating the distance for each path.
3. The ant chooses the shortest possible path to the next undiscovered food source.

The method assumes a small grid size, making brute force a feasible approach.

Both scripts track the ant's progress and display the shortest path as it moves between food sources.

## Reference 

For more information on pathfinding algorithms or improving your own simulation, you can refer to common algorithms like **Dijkstra's Algorithm** or **A* Search** for more optimized pathfinding strategies.

