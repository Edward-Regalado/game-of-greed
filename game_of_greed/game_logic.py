
from random import randint
from collections import Counter
#import sys
#from typing import Collection, MappingView
"""
commented out our code and brought in source code to do lab4
"""


class GameLogic:
    @staticmethod
    def roll_dice(num=6):
        # version_1

        return tuple([randint(1, 6) for _ in range(num)])

    @staticmethod
    def calculate_score(dice):
        """
        dice is a tuple of integers that represent the user's selected dice pulled out from current roll
        """
        # version_1

        if len(dice) > 6:
            raise Exception("Cheating Cheater!")

        counts = Counter(dice)

        if len(counts) == 6:
            return 1500

        if len(counts) == 3 and all(val == 2 for val in counts.values()):
            return 1500

        score = 0

        ones_used = fives_used = False

        for num in range(1, 6 + 1):

            pip_count = counts[num]

            if pip_count >= 3:

                if num == 1:

                    ones_used = True

                elif num == 5:

                    fives_used = True

                score += num * 100

                # handle 4,5,6 of a kind
                pips_beyond_3 = pip_count - 3

                score += score * pips_beyond_3

                # bug if 2 threesomes? Let's test it

                # 1s are worth 10x
                if num == 1:
                    score *= 10

        if not ones_used:
            score += counts.get(1, 0) * 100

        if not fives_used:
            score += counts.get(5, 0) * 50

        return score

    @staticmethod
    def validate_keepers(roll, keepers):
        # version_3

        return not Counter(keepers) - Counter(roll)

    @staticmethod
    def get_scorers(dice):
        # version_3

        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        scorers = []

        for i in range(len(dice)):
            sub_roll = dice[:i] + dice[i + 1 :]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                scorers.append(dice[i])

        return tuple(scorers)




#Original Group Code

# class GameLogic:

#     def __init__(self, dice_left=6, score=0):
#         self.dice_left = dice_left
#         self.current_round = current_round
#         self.score = score

#     def greeting(self):
#         print("Welcome to Game of Greed!")

#     def play_game(self):
#         self.greeting()
#         user_name = input("wanna play? type 'y' or 'yes' to roll > ")
#         if user_name == y or yes:
#             self.dice_kept(self.roll_dice(self.dice_left))

#     def exit_game(self):
#       name = input('Please Enter your Name: ')
#       while end_game != 'q':
#           print(f'{name}, please press q to quit!')
#           end_game = input('> ')
#       quit_game('Thanks for Playing!')

#     def quit_game(message):
#       sys.exit(message)

#     if __name__ == '__main__':
#         try:
#             exit_game()
#         except KeyboardInterrupt:
#             quit_game('Keyboard Inturrupt Detected!')

#     @staticmethod
#     def calculate_score(scoring_list):
#         score = 0
#         counter = Counter(scoring_list).most_common()

#         if len(counter) == 6:
#             score += 1500
#         elif len(counter) == 3 and counter[0][1] == 2 and counter[1][1] == 2 and counter[2][1] == 2:
#             score += 1500
#         else:
#             for i in counter:
#                 if i[0] == 1:
#                     if i[1] == 1:
#                         score += 100
#                     elif i[1] == 2:
#                         score += 200
#                     elif i[1] == 3:
#                         score += 1000
#                     elif i[1] == 4:
#                         score += 2000
#                     elif i[1] == 5:
#                         score += 3000
#                     else:
#                         score += 4000

#                 elif i[0] == 5:
#                     if i[1] == 1:
#                         score += 50
#                     elif i[1] == 2:
#                         score += 100
#                     elif i[1] == 3:
#                         score += 500
#                     elif i[1] == 4:
#                         score += 1000
#                     elif i[1] == 5:
#                         score += 1500
#                     else:
#                         score += 2000

#                 elif i[0] == 2 or 3 or 4 or 6:
#                     if i[1] == 3:
#                         score += (i[0] * 100)
#                     elif i[1] == 4:
#                         score += (i[0] * 200)
#                     elif i[1] == 5:
#                         score += (i[0] * 300)
#                     elif i[1] == 6:
#                         score += (i[0] * 400)

#         return score

#     @staticmethod
#     def validate_keepers(roll, keepers):
#         roll_counter = Counter(roll)
#         keepers_counter = Counter(keepers)
#         return len(keepers_counter - roll_counter) == 0


#     @staticmethod
#     def roll_dice(dice_left):
        
#         roll = tuple(random.randint(1, 6) for i in range(dice_left))

#         return roll

    
