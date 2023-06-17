def check_win(board, player):
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False

def get_next_move(board, player):

    for i in range(3):
        for j in range(3):
            if board[i][j] == -1:
                
                board[i][j] = player
                if check_win(board, player):
                    return [player, i, j]
                
                board[i][j] = -1
    
    return ['N']


player, n = map(int, input().split())
board = [[-1] * 3 for _ in range(3)]
for i in range(n):
    p, x, y = map(int, input().split())
    board[x][y] = p

next_move = get_next_move(board, player)

print(*next_move)
