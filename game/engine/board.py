def get_board(cells):
    board = [[{"symbol": None} for _ in range(3)] for _ in range(3)]

    for cell in cells:
        board[cell.row][cell.col] = {
            "symbol": cell.symbol,
            "player": cell.player_name
        }

    return board