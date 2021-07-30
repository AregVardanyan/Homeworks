import random
import time


def show(game_list):
    print(f"{game_list[0]}  |  {game_list[1]}  |  {game_list[2]}\n"
          "-------------\n"
          f"{game_list[3]}  |  {game_list[4]}  |  {game_list[5]}\n"
          "-------------\n"
          f"{game_list[6]}  |  {game_list[7]}  |  {game_list[8]}\n")


def update(game_list):
    new_list = []
    for i in game_list:
        if type(i) == int:
            new_list.append(i)
    return new_list


def check(game_list):
    if (game_list[0:3].count("❌") == 3 or game_list[3:6].count("❌") == 3 or game_list[6:].count("❌") == 3 or
            game_list[0:7:3].count("❌") == 3 or game_list[1:8:3].count("❌") == 3 or game_list[2::3].count("❌") == 3 or
            game_list[::4].count("❌") == 3 or game_list[2:7:2].count("❌") == 3):
        return 1
    if (game_list[0:3].count("⭕") == 3 or game_list[3:6].count("⭕") == 3 or game_list[6:].count("⭕") == 3 or
            game_list[0:7:3].count("⭕") == 3 or game_list[1:8:3].count("⭕") == 3 or game_list[2::3].count("⭕") == 3 or
            game_list[::4].count("⭕") == 3 or game_list[2:7:2].count("⭕") == 3):
        return -1
    return 0


def game():
    game_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print("Welcome to the game:")
    turn = random.choice([0, 1])
    print("Choosing turn...")
    time.sleep(2)
    show(game_list)
    for i in range(9):
        if (turn + i) % 2 == 1:
            your_choice = int(input(f"Input from {update(game_list)}:"))
            while not (your_choice in update(game_list)):
                your_choice = int(input("Wrong number"))
            game_list[your_choice] = "❌"
            show(game_list)
            time.sleep(0.5)
            if check(game_list) == 1:
                print("You win:")
                break
            time.sleep(0.5)
        elif (turn + i) % 2 == 0:
            computer_choice = random.choice(update(game_list))
            game_list[computer_choice] = "⭕"
            show(game_list)
            time.sleep(1)
            if check(game_list) == -1:
                print("Fu** you you lose:")
                break
            time.sleep(0.5)
    else:

        print("Draw")


game()
