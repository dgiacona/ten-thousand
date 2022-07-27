from collections import Counter
import random

class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def calculate_score(roll):
        banked_score = tuple(roll)
        if banked_score == ():
            return 0
        elif banked_score == (1,):
            return 100
        elif banked_score == (1, 1):
            return 200
        elif banked_score == (1, 1, 1):
            return 1000
        elif banked_score == (1, 1, 1, 1):
            return 2000
        elif banked_score == (1, 1, 1, 1, 1):
            return 3000
        elif banked_score == (1, 1, 1, 1, 1, 1):
            return 4000
        elif banked_score == (2,):
            return 0
        elif banked_score == (2,2):
            return 0
        elif banked_score == (2,2,2):
            return 200
        elif banked_score == (2,2,2,2):
            return 400
        elif banked_score == (2,2,2,2,2):
            return 600
        elif banked_score == (2,2,2,2,2,2):
            return 800
        elif banked_score == (3,):
            return 0
        elif banked_score == (3,3):
            return 0
        elif banked_score == (3,3,3):
            return 300
        elif banked_score == (3,3,3,3):
            return 600
        elif banked_score == (3,3,3,3,3):
            return 900
        elif banked_score == (3,3,3,3,3,3):
            return 1200
        elif banked_score == (4,):
            return 0
        elif banked_score == (4,4):
            return 0
        elif banked_score == (4,4,4):
            return 400
        elif banked_score == (4,4,4,4):
            return 800
        elif banked_score == (4,4,4,4,4):
            return 1200
        elif banked_score == (4,4,4,4,4,4):
            return 1600
        elif banked_score == (5,):
            return 50
        elif banked_score == (5,5):
            return 100
        elif banked_score == (5,5,5):
            return 500
        elif banked_score == (5,5,5,5):
            return 1000
        elif banked_score == (5,5,5,5,5):
            return 1500
        elif banked_score == (5,5,5,5,5,5):
            return 2000
        elif banked_score == (6,):
            return 0
        elif banked_score == (6,6):
            return 0
        elif banked_score == (6,6,6):
            return 600
        elif banked_score == (6,6,6,6):
            return 1200
        elif banked_score == (6,6,6,6,6):
            return 1800
        elif banked_score == (6,6,6,6,6,6):
            return 2400
        elif banked_score == (1,2,3,4,5,6):
            return 1500
        elif banked_score == (2,2,3,3,4,6):
            return 0
        elif banked_score == (2,2,3,3,6,6):
            return 1500
        elif banked_score == (1,1,1,2,2,2):
            return 1200

    @staticmethod
    def roll_dice(dice):
        roll = []
        for i in range(dice):
            roll.append(random.randint(0,6))
            return tuple(roll)
