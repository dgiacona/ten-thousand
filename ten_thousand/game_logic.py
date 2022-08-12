from collections import Counter
import random


class GameLogic:

    def __init__(self):
        pass

    @staticmethod
    def calculate_score(roll):

        roll_count = Counter(roll)

        if len(roll) == 0:
            return 0

        if len(roll) == 1:
            if roll_count[1] == 1:
                print("One 1: 100pts")
                return 100
            elif roll_count[5] == 1:
                return 50
            else:
                return 0

        if len(roll) == 2:
            if roll_count[1] == 2:
                return 200
            elif roll_count[5] == 2:
                return 100
            else:
                return 0

        if len(roll) == 3:
            if roll_count[1] == 3:
                return 1000
            elif roll_count[roll[0]] == 3:
                return roll[0] * 100

        if len(roll) == 4:
            if roll_count[1] == 4:
                return 2000
            if roll_count[roll[0]] == 4:
                return (roll[0] * 100) * (len(roll) - 2)

        if len(roll) == 5:
            if roll_count[1] == 5:
                return 3000
            elif roll_count[roll[0]] == 5:
                return (roll[0] * 100) * (len(roll) - 2)

        if len(roll) == 6:
            if roll_count[1] == 6:
                return 4000
            elif roll_count[roll[0]] == 6:
                return (roll[0] * 100) * (len(roll) - 2)

            # 2x 3 of a kind
            for i in range(6):
                if roll_count[i] == 3:
                    for i in range(i + 1, 6):
                        if roll_count[i] == 3:
                            return 1200
                        else:
                            return i * 100

            # Straight
            if roll == (1, 2, 3, 4, 5, 6):
                return 1500

            # 3 pair
            pair_count = 0
            for i in range(7):
                if roll_count[i] == 2:
                    pair_count += 1
            if pair_count == 3:
                return 1500
            else:
                return 0

    @staticmethod
    def roll_dice(dice):
        print(f"Rolling {dice} dice...")
        roll = []
        for _ in range(dice):
            roll.append(str(random.randint(1, 6)))

        formatted_roll = " ".join(roll)
        roll_output = print(f"*** {formatted_roll} ***")
        # result = tuple(roll)
        # print(f" *** {result} ***") # TODO get rid of ()
        return roll_output


def play():
    choice = invite_to_play()

    if choice == "y":
        start_game()
    else:
        decline_game()


def invite_to_play():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    wanna_play = input("> ")
    return wanna_play


def start_game():
    round_num = 1
    max_round = 3
    total_points = 0
    remaining_dice = 6
    while round_num <= max_round:
        new_points, dice_left_to_roll = do_round(round_num, remaining_dice)
        remaining_dice = dice_left_to_roll
        total_points += new_points
        print(f"Total score is {total_points} points")
        round_num += 1
    print(f"Thanks for playing. You earned {total_points} points")


def decline_game():
    print("OK. Maybe another time")
    exit()


def do_round(round_num, remaining_dice):
    print(f"Starting round {round_num}")
    roll_display = GameLogic.roll_dice(remaining_dice)
    # print(roll_display)
    kept_dice = offer_to_keep()
    dice_left_after_keep = remaining_dice - len(kept_dice)
    unbanked = GameLogic.calculate_score(kept_dice)
    round_score = roll_bank_quit(unbanked, dice_left_after_keep, round_num)
    round_result = []
    round_result.append(round_score)
    round_result.append(dice_left_after_keep)
    print(round_result)
    return round_result


def offer_to_keep():
    print("Enter dice to keep, or (q)uit:")
    keeps = input("> ")
    if keeps == "q":
        print("Thanks for playing. You earned 0 points")
        exit()
    to_bank = keeps.split()
    int_bank = []
    for i in range(len(to_bank)):
        int_bank.append(int(to_bank[i]))
    return int_bank


def roll_bank_quit(score, dice_left, round_num):
    print(f"You have {score} unbanked points and {dice_left} dice remaining")
    print("(r)oll again, (b)ank your points or (q)uit:")
    r_b_q = input("> ")
    if r_b_q == "q":
        print("Ok, thanks for playing.")
        exit()
    elif r_b_q == "b":
        print(f"You banked {score} points in round {round_num}")
        return score
    elif r_b_q == "r":
        # roll again? TODO figure out how to roll again
        pass
    else:
        print("That's an invalid response. Game over.")
        exit()


if __name__ == '__main__':
    play()
