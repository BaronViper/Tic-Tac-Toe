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
                        valid_choice = logic.play_turn(grid_data=grid_data, player_symbol=player_symbol)
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
            current_player = 'X'
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
                        valid_choice = logic.play_turn(grid_data=grid_data, player_symbol=current_player)
                        if current_player == 'X':
                            current_player = 'O'
                        elif current_player == 'O':
                            current_player = 'X'
                        self.print_table(grid_data=grid_data)

            if no_spaces:
                print("Game Over. Tie!")
                game_on = False
            else:
                print(f"Game Over. Winner is {winner}")
                game_on = False

