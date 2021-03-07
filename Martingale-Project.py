"""Testing Martingale Betting Strategy
Roulette: American Roulette with 38 slots with numbers 1-36, 0, and 00
Betting Conditions: Betting on black"""

import numpy as np
import matplotlib.pyplot as plt

def get_spin_result(win_prob):
    result = False
    if np.random.random() <= win_prob:
        result = True  
    return result  

def test_code():  
    win_prob = 0.474 
    print(get_spin_result(win_prob)) 
    game_results = simulator()
    
def simulator_1(round_num, spin_num):
    """Simulate the Martingale betting strategy for unlimited funds.
       bet_amount resets to 1 everytime one wins. It however doubles whenever one loses.
       spin_winnings is the net profit or loss after every spin.
    """
    spin_winnings = 0
    z = []
    for round in range(1,round_num):
        print("\nround:",round)
        spin_winnings = 0
        bet_amount = 1
        l = [0]
        for spin in range(1,spin_num):
            print("spin:",spin)
            if spin_winnings <80:
                if get_spin_result(0.474)==True:
                    spin_winnings = spin_winnings + bet_amount
                    bet_amount = 1
                    print("you just won")
                    print("spin_winnings:",spin_winnings)  
                else:
                    spin_winnings = spin_winnings - bet_amount
                    bet_amount = 2*bet_amount
                    print("you just lost.")
                    print("spin_winnings:",spin_winnings) 
                l.append(spin_winnings)
            else:
                spin_winnings = spin_winnings       
                print("spin_winnings:",spin_winnings)
                l.append(spin_winnings)
        
        z.append(l)
    print('z list:',z)
    print(type(z))
    return z
       
def simulator_2(round_num, spin_num):
    """Simulate the Martingale betting strategy for a limited fund of @256.
       bet_amount resets to 1 everytime one wins. It however doubles whenever one loses.
       spin_winnings is the net profit or loss after every spin.
    """
    m = []
    print("You have $256 in your bank!! You can bet as long as you have money in your bank!")
    for round in range(1,round_num):
        print("\nround:",round)
        spin_winnings = 0
        bet_amount = 1
        bank_roll = 256
        l = [0]
        for spin in range(1,spin_num):
            print("\nspin:",spin)
            print("bet_amount", bet_amount)
            if spin_winnings < 80 and bank_roll > 0 :
                if get_spin_result(0.474)==True:
                    spin_winnings = spin_winnings + bet_amount
                    bank_roll = bank_roll + bet_amount
                    print("you just won")
                    print("spin_winnings:",spin_winnings)
                    print("bank_roll",bank_roll)
                    bet_amount = 1
                    print("bet_amount changed to", bet_amount)
                else:
                    spin_winnings = spin_winnings - bet_amount
                    bank_roll = bank_roll - bet_amount
                    bet_amount = 2*bet_amount
                    print("bet_amount changed to",bet_amount)
                    print("you just lost.")
                    print("bank_roll",bank_roll)
                    print("spin_winnings:",spin_winnings) 
                l.append(spin_winnings)
            else:
                spin_winnings = spin_winnings
                print("spin_winnings:",spin_winnings)
                l.append(spin_winnings)
        
        m.append(l)
    print('m list:',m)
    print(type(m))
    return m
       
def figure1_graph(z):
    numpy_z = np.array(z)
    for i in numpy_z:
        plt.plot(i)
    axes = plt.gca()
    axes.set_xlim([0,300])
    axes.set_ylim([-150,100])
    plt.title("Figure 1 - Simulation of 10 episodes of 1000 sequential spins with unlimited funds")
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.legend(['round 1','round 2','round 3','round 4','round 5','round 6','round 7','round 8','round 9','round 10',])
    plt.show()

def figure2_graph(z):
    numpy_z = np.array(z).T
    mean = np.mean(numpy_z, axis = 1)
    std = np.std(numpy_z, axis = 1)
    upper_line_mean = mean + std
    lower_line_mean = mean - std
    for i in numpy_z:
        plt.plot(mean, 'r-')
        plt.plot(upper_line_mean,'g-')
        plt.plot(lower_line_mean,'b-')
    axes = plt.gca()
    axes.set_xlim([0,300])
    axes.set_ylim([-300,200])
    plt.title("Figure 2 - Simulation of 1000 episodes of 1000 sequential spins with unlimited funds")
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.legend(['mean','above line','below line'])
    plt.show()

def figure3_graph(z):
    numpy_z = np.array(z).T
    median = np.median(numpy_z, axis = 1)
    std = np.std(numpy_z, axis = 1)
    upper_line_median = median + std
    lower_line_median = median - std
    for i in numpy_z:
        plt.plot(median, 'r-')
        plt.plot(upper_line_median,'g-')
        plt.plot(lower_line_median,'b-')
    axes = plt.gca()
    axes.set_xlim([0,300])
    axes.set_ylim([-256,100])
    plt.title("Figure 3 - Simulation of 1000 episodes of 1000 sequential spins with unlimited funds")
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.legend(['median','above line','below line'])
    plt.show()

def figure4_graph(m):
    numpy_m = np.array(m).T
    std = np.std(numpy_m, axis = 1)
    mean = np.mean(numpy_m, axis = 1)
    std = np.std(numpy_m, axis = 1)
    upper_line_mean = mean + std
    lower_line_mean = mean - std
    for i in numpy_m:
        plt.plot(mean, 'r-')
        plt.plot(upper_line_mean,'g-')
        plt.plot(lower_line_mean,'b-')
    axes = plt.gca()
    axes.set_xlim([0,300])
    axes.set_ylim([-256,200])
    plt.title("Figure 4 - Simulation of 1000 episodes of 1000 sequential spins with funds of $256")
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.legend(['mean','above line','below line'])
    plt.show()

def figure5_graph(m):
    numpy_m = np.array(m).T
    std = np.std(numpy_m, axis = 1)
    median = np.median(numpy_m, axis = 1)
    upper_line_median = median + std
    lower_line_median = median - std
    for i in numpy_m:
        plt.plot(median, 'r-')
        plt.plot(upper_line_median,'g-')
        plt.plot(lower_line_median,'b-')
    axes = plt.gca()
    axes.set_xlim([0,300])
    axes.set_ylim([-256,100])
    plt.title("Figure 5 - Simulation of 1000 episodes of 1000 sequential spins with funds of $256")
    plt.xlabel("Number of Spins")
    plt.ylabel("Winnings")
    plt.legend(['median','above line','below line'])
    plt.show()

def run_exp1_part1(z):
    figure1_graph(z)

def run_exp1_part2(z):
    figure2_graph(z)
    figure3_graph(z)
    
def run_exp2(m):
    figure4_graph(m)
    figure5_graph(m)

"""run the simulator 10 times, each run consists of 1000 spins"""
z = simulator_1(11,1000)
run_exp1_part1(z)

"""run the simulator 1000 times, each run consists of 1000 spins"""
z = simulator_1(1001,1000)
run_exp1_part2(z)

"""run the simulator 1000 times, each run consists of 1000 spins"""
m = simulator_2(1001,1000)
run_exp2(m)

