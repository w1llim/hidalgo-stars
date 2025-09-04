# Noughts-and-crosses using the imperative paradigm

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    return all(all(cell != " " for cell in row) for row in board)


# main program
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

while True:
    print_board(board)

    row = int(input(f"Player {current_player}, enter row (0-2): "))
    col = int(input(f"Player {current_player}, enter column (0-2): "))

    if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        else:
            current_player = "O" if current_player == "X" else "X"
    else:
        print("Invalid move. Try again.")


