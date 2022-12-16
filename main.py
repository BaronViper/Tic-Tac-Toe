from game import TicTacToe
import assets

run = True

while run:
    print(assets.logo)
    valid_mode = False
    tictactoe = TicTacToe()
    while not valid_mode:
        mode = (input("Single-player(1) or Two-player(2) mode? Enter the number associated with your choice:\n"))

        if mode == "1" or mode == "2":
            valid_mode = True
        else:
            print("Invalid choice. Make sure to enter '1' or '2' for your desired game mode.")

    if mode == "1":
        print("Single-player mode selected.")
        valid_player = False
        while not valid_player:
            player = (input("Pick your symbol. X or O?\n")).lower()
            if player == "x" or player == "o":
                valid_player = True
                if player == 'x':
                    print("Symbol 'X' selected. Starting game...\n")

                    tictactoe.single_player_start(player_symbol=player)



                elif player == 'o':
                    print("Symbol 'O' selected. Starting game...\n")

                    tictactoe.single_player_start(player_symbol=player)

            else:
                print("Invalid choice. Enter 'X' or 'O' to pick your symbol of choice.")

    elif mode == "2":
        print("Two-player mode selected.")
        valid_player = False
        while not valid_player:
            player1 = (input("Player 1, pick your symbol. X or O?\n")).lower()
            if player1 == "x" or player1 == "o":
                valid_player = True
                if player1 == 'x':
                    print("Symbol 'X' selected. Starting game...\n")
                    player2 = 'o'

                    tictactoe.multi_player_start(player1_symbol=player1, player2_symbol=player2)

                elif player1 == 'o':
                    print("Symbol 'O' selected. Starting game...\n")
                    player2 = 'x'

                    tictactoe.multi_player_start(player1_symbol=player1, player2_symbol=player2)


            else:
                print("Invalid choice. Enter 'X' or 'O' to pick your symbol of choice.")

    valid_retry = False
    while not valid_retry:
        play_again = (input("New match? (Y) or (N):\n")).lower()
        if play_again != 'y' and play_again != 'n':
            print("Invalid choice. Enter 'Y' to play a new match or 'N' to end.\n")
        elif play_again == 'y':
            run = True
            valid_retry = True
        elif play_again == 'n':
            run = False
            valid_retry = True
