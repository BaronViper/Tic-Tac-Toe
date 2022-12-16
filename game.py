import game_logic
import assets
import os
import time

class TicTacToe:
    def print_table(self, grid_data):
        grid = f"""
             |     |     
          {grid_data[0][0]}  |  {grid_data[0][1]}  |  {grid_data[0][2]}  
        _____|_____|_____
             |     |     
          {grid_data[1][0]}  |  {grid_data[1][1]}  |  {grid_data[1][2]}  
        _____|_____|_____
             |     |     
          {grid_data[2][0]}  |  {grid_data[2][1]}  |  {grid_data[2][2]}  
             |     |     
        """
        print(grid)

    def single_player_start(self, player_symbol):
        logic = game_logic.TictactoeLogic()
        print(f"Here is the board layout. Keep note of the numbers and enter them according to your "
              f"desired grid space!\n{assets.grid}")

        if player_symbol == 'x':
            ai_symbol = 'O'
            player_symbol = 'X'
            starting_player = "player"
        else:
            ai_symbol = 'X'
            player_symbol = 'O'
            starting_player = 'ai'
        grid_data = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        game_on = True
        while game_on:
            winner = ()
            round_on = True
            while round_on:
                empty_spaces = logic.calculate_spaces(grid_data=grid_data)
                winner = logic.calculate_winner(grid_data=grid_data)

                if empty_spaces == 0:
                    round_on = False
                    no_spaces = True
                elif winner == 'X' or winner == 'O':
                    round_on = False
                    no_spaces = False
                elif empty_spaces != 0:
                    valid_choice = False
                    while not valid_choice:
                        player_choice = input(
                            "Enter a number according to the desired grid space.\n")
                        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                        if player_choice not in numbers:
                            print("Invalid option. Please select a number from 1-9")
                        else:
                            player_choice = int(player_choice)
                            print(player_choice)
                            if player_choice == 1 or player_choice == 2 or player_choice == 3:
                                minus_index = 1
                                row_no = 0
                            elif player_choice == 4 or player_choice == 5 or player_choice == 6:
                                minus_index = 4
                                row_no = 1
                            elif player_choice == 7 or player_choice == 8 or player_choice == 9:
                                minus_index = 7
                                row_no = 2

                            if grid_data[row_no][player_choice - minus_index] != ' ':
                                print(
                                    "Invalid option. Space is already occupied. Please select another number from 1-9")
                            else:
                                valid_choice = True
                                grid_data[row_no][player_choice - minus_index] = f'{player_symbol}'
                                self.print_table(grid_data=grid_data)
            if no_spaces:
                print("Game Over. Tie!")
                game_on = False
            else:
                print(f"Game Over. Winner is {winner}")
                game_on = False

    def multi_player_start(self, player1_symbol, player2_symbol):
        logic = game_logic.TictactoeLogic()
        print(f"Here is the board layout. Keep note of the numbers and enter them according to your "
              f"desired grid space!\n{assets.grid}")
        if player1_symbol == 'x':
            player2_symbol = 'O'
            player1_symbol = 'X'
            starting_player = "1"
        else:
            player2_symbol = 'X'
            player1_symbol = 'O'
            starting_player = '2'
        grid_data = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        game_on = True
        while game_on:
            round_on = True
            while round_on:
                empty_spaces = logic.calculate_spaces(grid_data=grid_data)
                winner = logic.calculate_winner(grid_data=grid_data)
                if empty_spaces == 0 or winner != ():
                    round_on = False
                elif empty_spaces != 0:
                    for turn in range(1, 3):
                        if turn == 1:
                            current_player = player1_symbol
                        elif turn == 2:
                            current_player = player2_symbol
                            while not valid_choice:
                                player_choice = input(
                                    f"Player{starting_player}({current_player}), Enter a number according to the desired grid space.\n")
                                numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                                if player_choice not in numbers:
                                    print("Invalid option. Please select a number from 1-9")
                                else:
                                    player_choice = int(player_choice)
                                    print(player_choice)
                                    if player_choice == 1 or player_choice == 2 or player_choice == 3:
                                        minus_index = 1
                                        row_no = 0
                                    elif player_choice == 4 or player_choice == 5 or player_choice == 6:
                                        minus_index = 4
                                        row_no = 1
                                    elif player_choice == 7 or player_choice == 8 or player_choice == 9:
                                        minus_index = 7
                                        row_no = 2

                                    if grid_data[row_no][player_choice - minus_index] != ' ':
                                        print(
                                            "Invalid option. Space is already occupied. Please select another number from "
                                            "1-9")
                                    else:
                                        valid_choice = True
                                        grid_data[row_no][player_choice - minus_index] = f'{current_player}'
                                        self.print_table(grid_data=grid_data)
                                        os.system('cls')

