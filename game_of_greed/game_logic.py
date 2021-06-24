import random
from collections import Counter

class GameLogic:

    def __init__(self, dice_left):
        self.dice_left = 6


    @staticmethod
    def roll_dice(dice_left):
        if dice_left == None:
            dice_left = self.dice_left
        if dice_left == 0:
            return() 
        roll = tuple(random.randint(1, 6) for i in range(dice_left))
        print(f'You rolled a {roll}')

        return roll

    #roll_dice(6)
