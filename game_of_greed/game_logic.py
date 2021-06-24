import random
from collections import Counter



class GameLogic:

    def __init__(self, dice_left, current_round):
        self.dice_left = 6
        self.current_round = current_round
        self.bank = 0

    def greeting(self):
        print("Welcome to Game of Greed!")

    def play_game(self):
        self.greeting()
        user_name = input("wanna play? type 'y' or 'yes' to roll > ")
        if user_name == y or yes:
            self.dice_kept(self.roll_dice(self.dice_left))


    @staticmethod
    def calculate_score(roll_results):
        score = 0
        chosen_list = list(input("select dice to save > "))
        chosen_list = [int(i) for i in chosen_list]
        scoring_list = list((Counter(roll_results) & Counter(chosen_list)).elements())
        counter = Counter(scoring_list).most_common()
        

        if len(counter) == 6:
            score += 1500
        if len(counter) == 3 and counter[0][1] == 2 and counter[1][1] == 2 and counter[2][1] == 2:
            score += 1500
        if len(counter) == 1 and counter[0][0] == 5  and counter[0][1] == 1:
            score += 50
        if len(counter) == 1 and counter[0][0] == 5  and counter[0][1] == 2:
            score += 100
        if len(counter) == 1 and counter[0][0] == 5  and counter[0][1] == 6:
            score += 2000
        if len(counter) == 1 and counter[0][0] == 1  and counter[0][1] == 1:
            score += 100
        if len(counter) == 1 and counter[0][0] == 1  and counter[0][1] == 6:
            score += 4000
        if len(counter) == 1 and counter[0][0] == 1  and counter[0][1] == 2:
            score += 200

        
        
        return score





    @staticmethod
    def roll_dice(dice_left):
        if dice_left == None:
            dice_left = self.dice_left
        if dice_left == 0:
            return() 
        roll = tuple(random.randint(1, 6) for i in range(dice_left))
        print(f'You rolled a {roll}')

        return roll

    
