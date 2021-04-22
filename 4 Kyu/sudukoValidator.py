def validSolution(board):

    for i in range(len(board)):
        hadd = 0
        vadd = 0
        for j in range(len(board)):
            #vertical check
            vadd += board[j][i]
            #horizontal check
            hadd += board[i][j]
            #numbers check
            if board[i][j] < 1 or board[i][j] > 9:
                print(1)
                return False
        if vadd != 45 or hadd != 45:
            print (2)
            print (vadd)
            print (hadd)
            return False
    for i in range(3):
        for j in range(3):
            gadd = 0
            for k in range(3):
                for l in range(3):
                    gadd += board[i*3+k][j*3+l]
                    if board[i][j] < 1 or board[i][j] > 9:
                        print (3)
                        return False
            if gadd != 45:
                return False
    return True 


board = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
         [6, 7, 2, 1, 9, 5, 3, 4, 8],
         [1, 9, 8, 3, 4, 2, 5, 6, 7],
         [8, 5, 9, 7, 6, 1, 4, 2, 3],
         [4, 2, 6, 8, 5, 3, 7, 9, 1],
         [7, 1, 3, 9, 2, 4, 8, 5, 6],
         [9, 6, 1, 5, 3, 7, 2, 8, 4],
         [2, 8, 7, 4, 1, 9, 6, 3, 5],
         [3, 4, 5, 2, 8, 6, 1, 7, 9]]

# print(validSolution(board))