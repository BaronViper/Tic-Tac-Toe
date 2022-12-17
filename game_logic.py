class TictactoeLogic:
    def calculate_spaces(self, grid_data):
        empty_spaces = 0
        for n in grid_data[0]:
            if n == ' ':
                empty_spaces += 1
        for n in grid_data[1]:
            if n == ' ':
                empty_spaces += 1
        for n in grid_data[2]:
            if n == ' ':
                empty_spaces += 1

        return empty_spaces

    def play_turn(self, grid_data, player_symbol):
        player_choice = input(
            f"({player_symbol}), Enter a number according to the "
            f"desired grid space.\n")
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        if player_choice not in numbers:
            print("Invalid option. Please select a number from 1-9")
        else:
            player_choice = int(player_choice)
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
                grid_data[row_no][player_choice - minus_index] = f'{player_symbol}'
                valid_choice = True
        return valid_choice

    def calculate_winner(self, grid_data):
        winner = ()
        # calculate horizontal
        for row in grid_data:
            if winner != ():
                pass
            elif row == ['X', 'X', 'X'] or row == ['O', 'O', 'O']:
                winner = row[0]

        # calculate vertical
        for n in range(3):
            if winner != ():
                pass
            elif grid_data[0][n] == grid_data[1][n] == grid_data[2][n]:
                winner = grid_data[0][n]

        # calculate diagonal
        if winner != ():
            pass
        elif grid_data[0][0] == grid_data[1][1] == grid_data[2][2]:
            winner = grid_data[0][0]
        elif grid_data[0][2] == grid_data[1][1] == grid_data[2][0]:
            winner = grid_data[0][2]

        return winner
