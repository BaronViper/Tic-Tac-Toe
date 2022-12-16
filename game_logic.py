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
