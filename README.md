###Martingale Betting Strategy Simulation

This project simulates the Martingale betting strategy on American Roulette, where the player bets on black. The simulation explores both unlimited and limited bankroll scenarios, providing insights into the effectiveness and risks of the Martingale system.

Table of Contents
Project Overview
Requirements
Usage
Simulation Details
Unlimited Funds Simulation
Limited Funds Simulation
Graphical Analysis
Figure 1 - Sequential Spins (Unlimited Funds)
Figure 2 & 3 - Mean and Median Analysis (Unlimited Funds)
Figure 4 & 5 - Mean and Median Analysis (Limited Funds)
License
Project Overview
The Martingale betting strategy is a popular but risky betting system where the player doubles their bet after every loss, resetting the bet after each win. This project simulates the Martingale strategy on an American Roulette table with 38 slots, including 0 and 00.

The project contains two primary simulation scenarios:

Unlimited Funds: The player has infinite funds and can continue betting indefinitely.
Limited Funds: The player has a fixed bankroll of $256 and must stop betting when funds are depleted.
Requirements
Python 3.x
NumPy
Matplotlib
You can install the required packages using pip:

bash
Copy code
pip install numpy matplotlib
Usage
To run the simulations, clone this repository and run the provided Python script:

bash
Copy code
git clone https://github.com/yourusername/martingale-roulette-simulation.git
cd martingale-roulette-simulation
python martingale_simulation.py
Simulation Details
Unlimited Funds Simulation
The simulator_1 function simulates the Martingale strategy with unlimited funds. The simulation runs for a specified number of rounds and spins per round. The player's bet doubles after each loss and resets after each win.

Limited Funds Simulation
The simulator_2 function simulates the strategy with a limited bankroll of $256. The player bets until they either reach a target profit or run out of funds.

Graphical Analysis
The project generates several graphs to visualize the results of the simulations:

Figure 1 - Sequential Spins (Unlimited Funds)
Shows the results of 10 episodes, each consisting of 1000 sequential spins. It plots the player's winnings over time.

Figure 2 & 3 - Mean and Median Analysis (Unlimited Funds)
Figure 2: Plots the mean winnings with upper and lower bounds (standard deviation) across 1000 episodes of 1000 spins.
Figure 3: Plots the median winnings with upper and lower bounds (standard deviation) across 1000 episodes of 1000 spins.
Figure 4 & 5 - Mean and Median Analysis (Limited Funds)
Figure 4: Similar to Figure 2 but for the limited funds scenario.
Figure 5: Similar to Figure 3 but for the limited funds scenario.
License
This project is licensed under the MIT License. See the LICENSE file for details.
