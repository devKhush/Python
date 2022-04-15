import random


def decide_game_result(turn_player: str, turn_computer: str):
    if turn_player == 'Snake':
        if turn_computer == 'Gun':
            print("Computer chosed 'Gun'. You lose\n")
        elif turn_computer == 'Water':
            print("Computer chosed 'Water'. You won\n")
        else:
            print("Computer chosed 'Snake'. Match Draw\n")

    elif turn_player == 'Water':
        if turn_computer == 'Gun':
            print("Computer chosed 'Gun'. You won\n")
        elif turn_computer == 'Snake':
            print("Computer chosed 'Snake'. You lose\n")
        else:
            print("Computer chosed 'Water'. Match Draw\n")

    else:
        if turn_computer == 'Snake':
            print("Computer chosed 'Snake'. You won\n")
        elif turn_computer == 'Water':
            print("Computer chosed 'Water'. You lose\n")
        else:
            print("Computer chosed 'Gun'. Match Draw\n")


def Snake_Water_Gun_Game():

    halted = False
    while not halted:

        # Player turn
        player_options = {'s': 'Snake', 'g': 'Gun', 'w': 'Water'}
        print("Enter 'quit' for stop playing")
        player_turn = input(
            'Enter Snake(s), water(w) or gun(g): ').strip().lower()
        if player_turn == 'quit':
            halted = True
            continue
        if player_turn not in player_options.keys():
            print('Invalid Option. Enter Again\n')
            continue
        player_turn = player_options[player_turn]

        # Computer turn
        rand_num = random.randint(1, 3)
        computer_turn = {1: 'Snake', 2: 'Water', 3: 'Gun'}[rand_num]

        # Game result
        decide_game_result(turn_player=player_turn,
                           turn_computer=computer_turn)

    print('Thanks for Playing!')


if __name__ == "__main__":
    print()
    Snake_Water_Gun_Game()
