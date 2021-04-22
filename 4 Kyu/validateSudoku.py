import math

class Sudoku(object):
    def __init__(self, board):
        self.board = board
        
    def is_valid(self):
        if not isinstance(self.board, list):
            return False
        n = len(self.board)
        rootN = int(round(math.sqrt(n)))
        if rootN * rootN != n:
            return False
        isValidRow = lambda r : (isinstance(r, list) and
                                 len(r) == n and
                                 all(map(lambda x : type(x) == int, r)))
        if not all(map(isValidRow, self.board)):
            return False
        oneToN = set(range(1, n + 1))
        isOneToN = lambda l : set(l) == oneToN
        tranpose = [[self.board[j][i] for i in range(n)] for j in range(n)]
        squares = [[self.board[p+x][q+y] for x in range(rootN) 
                                         for y in range(rootN)] 
                                         for p in range(0, n, rootN)
                                         for q in range(0, n, rootN)] 
        return (all(map(isOneToN, self.board)) and
                all(map(isOneToN, tranpose)) and
                all(map(isOneToN, squares)))

board =[
        [7,8,4,  1,5,9,  3,2,6],
        [5,3,9,  6,7,2,  8,4,1],
        [6,1,2,  4,3,8,  7,5,9],
        
        [9,2,8,  7,1,5,  4,6,3],
        [3,5,7,  8,4,6,  1,9,2],
        [4,6,1,  9,2,3,  5,8,7],
        
        [8,7,6,  3,9,4,  2,1,5],
        [2,4,3,  5,6,1,  9,7,8],
        [1,9,5,  2,8,7,  6,3,4]
       ]

print(Sudoku(board).is_valid())