class TicTacToeBot:
    def ai_play(self, grid, ai_symbol, player_symbol):
        valid_play = True
        while valid_play:
            # Take center space
            if valid_play:
                if grid[1][1] == ' ':
                    grid[1][1] = ai_symbol
                    valid_play = False

            # Block horizontal
            if valid_play:
                row_count = -1
                for row in grid:
                    row_count += 1
                    if row.count(player_symbol) == 2 and ' ' in row:
                        grid[row_count][row.index(' ')] = ai_symbol
                        valid_play = False

            # Block vertical
            if valid_play:
                for n in range(3):
                    vert_list = [grid[0][n], grid[1][n], grid[2][n]]
                    if vert_list.count(player_symbol) == 2 and ' ' in vert_list:
                        grid[vert_list.index(' ')][n] = ai_symbol
                        valid_play = False

            # Block first diagonal
            if valid_play:
                diagonal = [grid[0][0], grid[1][1], grid[2][2]]
                if diagonal.count(player_symbol) == 2 and ' ' in diagonal:
                    grid[diagonal.index(' ')][diagonal.index(' ')] = ai_symbol
                    valid_play = False

            # Block second diagonal
            if valid_play:
                diagonal = [grid[0][2], grid[1][1], grid[2][0]]
                if diagonal.count(player_symbol) == 2 and ' ' in diagonal:
                    grid[diagonal.index(' ')][2-diagonal.index(' ')] = ai_symbol
                    valid_play = False

            # Finish horizontal
            if valid_play:
                row_count = -1
                for row in grid:
                    row_count += 1
                    if row.count(ai_symbol) == 2 and ' ' in row:
                        grid[row_count][row.index(' ')] = ai_symbol
                        valid_play = False

            # Finish vertical
            if valid_play:
                for n in range(3):
                    vert_list = [grid[0][n], grid[1][n], grid[2][n]]
                    if vert_list.count(ai_symbol) == 2 and ' ' in vert_list:
                        grid[vert_list.index(' ')][n] = ai_symbol
                        valid_play = False

            # Finish first diagonal
            if valid_play:
                diagonal = [grid[0][0], grid[1][1], grid[2][2]]
                if diagonal.count(ai_symbol) == 2 and ' ' in diagonal:
                    grid[diagonal.index(' ')][diagonal.index(' ')] = ai_symbol
                    valid_play = False

            # Finish second diagonal
            if valid_play:
                diagonal = [grid[0][2], grid[1][1], grid[2][0]]
                if diagonal.count(ai_symbol) == 2 and ' ' in diagonal:
                    grid[diagonal.index(' ')][2 - diagonal.index(' ')] = ai_symbol
                    valid_play = False

            # Add second horizontal
            if valid_play:
                row_count = -1
                for row in grid:
                    row_count += 1
                    if row.count(ai_symbol) == 1 and ' ' in row:
                        grid[row_count][row.index(' ')] = ai_symbol
                        valid_play = False

            # Finish vertical
            if valid_play:
                for n in range(3):
                    vert_list = [grid[0][n], grid[1][n], grid[2][n]]
                    if vert_list.count(ai_symbol) == 1 and ' ' in row:
                        grid[vert_list.index(' ')][n] = ai_symbol
                        valid_play = False




