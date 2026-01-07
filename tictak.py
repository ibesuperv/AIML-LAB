from copy import deepcopy



def print_board(board):
    print("\n BOARD \n")
    for row in board:
        print(" | ".join(row))
    print()

def check_winner(board):
    lines = []
    for r in range(3):
        lines.append(board[r])
        lines.append([board[0][r],board[1][r], board[2][r]])
    lines.append([board[0][0],board[1][1], board[2][2]])
    lines.append([board[0][2],board[1][1], board[0][2]])
    
    if ["X", "X", "X"] in lines:
        return "X"
    elif ["O", "O", "O"] in lines:
        return "O"
    for row in lines:
        if " " in row:
            return None
    return "Draw"
    
        
        
def dfs(board, player):
    winner = check_winner(board)
    if winner == "X":
        return 1
    if winner == "O":
        return -1
    if winner == "Draw":
        return 0
    
    scores = []
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                new_board = deepcopy(board)
                new_board[r][c] = player
                score = dfs(new_board, "O" if player == "X" else "X")
                scores.append(score)
                
    return max(scores) if player == "X" else min(scores)

def best_move(board):
    best_score = float('-inf')
    move = None
    for r in range(3):
        for c in range(3):
            if board[r][c] == " ":
                new_board = deepcopy(board)    
                new_board[r][c] = "X"
                score = dfs(new_board, "O")
                if score > best_score:
                    best_score = score
                    move = (r, c)
    return move

def start_game():
    print("TIC-TAC-TOE game.\n")
    print("You are O, AI is X.")
    board = [[" "] * 3 for _ in range(3)]
    print_board(board)
    while True:
        while True:
            try:
                r = int(input("Enter the Row"))
                c = int(input("Enter the col"))
                if board[r][c] == " ":
                    board[r][c] = "O"
                    break
                else:
                    print("That spot is already taken.")
            except:
                print("Invalid Place")
        if check_winner(board):
            print(" Result: ", check_winner(board))
            break
        print("AI is thinking")
        move = best_move(board)
        if move is None:
            print("AI has no slot")
            print(" Result: ", check_winner(board))
            break
        r, c = move
        board[r][c] = "X"
        print("AI placed X at: ", r, c)
        print_board(board)
        if check_winner(board):
            print(" Result: ", check_winner(board))
            break
        

start_game()