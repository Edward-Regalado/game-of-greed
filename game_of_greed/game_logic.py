import random
from collections import Counter



class GameLogic:

    def __init__(self, dice_left=6):
        self.dice_left = dice_left
        self.current_round = current_round
        self.bank = 0

    def greeting(self):
        print("Welcome to Game of Greed!")

    def play_game(self):
        self.greeting()
        user_name = input("wanna play? type 'y' or 'yes' to roll > ")
        if user_name == y or yes:
            self.dice_kept(self.roll_dice(self.dice_left))


    def get_saved_dice(roll_results):
        chosen_list = list(input("select dice to save > "))
        chosen_list = [int(i) for i in chosen_list]
        scoring_list = list((Counter(roll_results) & Counter(chosen_list)).elements())
        return scoring_list

    @staticmethod
    def calculate_score(scoring_list):
        score = 0
        counter = Counter(scoring_list).most_common()
        
        if len(counter) == 6:
            score += 1500
        elif len(counter) == 3 and counter[0][1] == 2 and counter[1][1] == 2 and counter[2][1] == 2:
            score += 1500
        else:
            for i in counter:
                if i[0] == 1:
                    if i[1] == 1:
                        score += 100
                    elif i[1] == 2:
                        score += 200
                    elif i[1] == 3:
                        score += 1000
                    elif i[1] == 4:
                        score += 2000
                    elif i[1] == 5:
                        score += 3000
                    else:
                        score += 4000

                elif i[0] == 5:
                    if i[1] == 1:
                        score += 50
                    elif i[1] == 2:
                        score += 100
                    elif i[1] == 3:
                        score += 500
                    elif i[1] == 4:
                        score += 1000
                    elif i[1] == 5:
                        score += 1500
                    else:
                        score += 2000  

                elif i[0] == 2 or 3 or 4 or 6:
                    if i[1] == 3:
                        score += (i[0] * 100)
                    elif i[1] == 4:
                        score += (i[0] * 200)
                    elif i[1] == 5:
                        score += (i[0] * 300)
                    elif i[1] == 6:
                        score += (i[0] * 400)      
        
        return score





    @staticmethod
    def roll_dice(dice_left):
        
        roll = tuple(random.randint(1, 6) for i in range(dice_left))
        print(f'You rolled a {roll}')

        return roll

    
