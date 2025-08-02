board = [' ' for _ in range(9)]
def print_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(p):
    return (
        (board[0] == board[1] == board[2] == p) or
        (board[3] == board[4] == board[5] == p) or
        (board[6] == board[7] == board[8] == p) or
        (board[0] == board[3] == board[6] == p) or
        (board[1] == board[4] == board[7] == p) or
        (board[2] == board[5] == board[8] == p) or
        (board[0] == board[4] == board[8] == p) or
        (board[2] == board[4] == board[6] == p)
    )

def play():
    turn = 'X'
    for _ in range(9):
        print_board()
        move = int(input(f"Player {turn}, enter position (1-9): ")) - 1
        if board[move] != ' ':
            print("Spot taken! Try again.")
            continue
        board[move] = turn
        if check_win(turn):
            print_board()
            print(f"Player {turn} wins!")
            return
        turn = 'O' if turn == 'X' else 'X'
    print_board()
    print("It's a draw!")

play()
