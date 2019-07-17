"""
Find probailty in Risk battle of attacker win

Attacker throw 3 dice, and defender 2 dice
They order results and compare highest attacker vs highest defender, then next highest
Attacker wins if his dice is higher, if not defender wins (ie. if they have same numbers defender wins)

Examples:
A: 651  D: 54 -> attacker wins both (6:5 and 5:4)
A: 611  D: 54 -> attacker wins 1 (6:5) and defender 1 (1:4)
"""
import random

DEBUG = False

"""

"""
def roll_die():
    return random.randint(1, 6)

def roll_dice(num_dice):
    dice_results = []

    for ix in range(num_dice):
        dice_results.append(roll_die())

    dice_results.sort(reverse=True)

    if (DEBUG):
        print(dice_results)

    return tuple(dice_results)

def risk_round(num_att, num_def):
    att_results = roll_dice(num_att)
    def_results = roll_dice(num_def)

    att_wins = 0

    for ix in range(min(num_att, num_def)):
        if att_results[ix] > def_results[ix]:
            att_wins += 1
    
    return att_wins

def risk_round_distribution_32():
    sample_size = 1000000
    att_wins = [0, 0, 0]

    for ix in range(sample_size):
        att_wins[risk_round(3, 2)] += 1

    print((att_wins[0]/sample_size, att_wins[1]/sample_size, att_wins[2]/sample_size))

def test():
    print(risk_round(3, 2))

#test()
risk_round_distribution_32()
