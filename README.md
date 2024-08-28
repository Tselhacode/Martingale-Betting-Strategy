# Martingale Betting Strategy Simulation

This project simulates the Martingale betting strategy on American Roulette, where the player bets on black. The simulation explores both unlimited and limited bankroll scenarios, providing insights into the effectiveness and risks of the Martingale system.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [Simulation Details](#simulation-details)
  - [Unlimited Funds Simulation](#unlimited-funds-simulation)
  - [Limited Funds Simulation](#limited-funds-simulation)
- [Graphical Analysis](#graphical-analysis)
  - [Figure 1 - Sequential Spins (Unlimited Funds)](#figure-1---sequential-spins-unlimited-funds)
  - [Figure 2 & 3 - Mean and Median Analysis (Unlimited Funds)](#figure-2--3---mean-and-median-analysis-unlimited-funds)
  - [Figure 4 & 5 - Mean and Median Analysis (Limited Funds)](#figure-4--5---mean-and-median-analysis-limited-funds)
- [License](#license)

## Overview

The Martingale betting strategy is a popular but risky betting system where the player doubles their bet after every loss and resets the bet after each win. This project simulates the Martingale strategy on an American Roulette table with 38 slots, including 0 and 00.

The project includes two primary simulation scenarios:
1. **Unlimited Funds**: The player has infinite funds and can continue betting indefinitely.
2. **Limited Funds**: The player has a fixed bankroll of $256 and must stop betting when funds are depleted.

## Requirements

- Python 3.x
- NumPy
- Matplotlib

To install the required packages, use:

```bash
pip install numpy matplotlib

```Usage
To run the simulations, clone this repository and run the provided Python script:

```bash
git clone https://github.com/yourusername/martingale-roulette-simulation.git
cd martingale-roulette-simulation
python martingale_simulation.py

