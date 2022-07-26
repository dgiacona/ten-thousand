from collections import Counter
import random

class GameLogic:
    def __init__(self):
        pass

    @staticmethod
    def calculate_score(dice_tuple):
        if dice_tuple == (1,):
            return 100