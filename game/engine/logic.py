def check_win(board):
    lines = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)],
    ]

    for a, b, c in lines:
        if (
            board[a[0]][a[1]]["symbol"] and
            board[a[0]][a[1]]["symbol"]
            == board[b[0]][b[1]]["symbol"]
            == board[c[0]][c[1]]["symbol"]
        ):
            return {
                "winner": board[a[0]][a[1]]["symbol"],
                "line": [a, b, c]
            }

    return None


def is_draw(board):
    return all(cell["symbol"] for row in board for cell in row)