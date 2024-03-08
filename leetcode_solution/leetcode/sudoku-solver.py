class Solution:
    def isvalid(self,x,y,n):
        for i in range(9):
            if n==self.board[i][y]:
                return False
        for i in range(9):
            if n==self.board[x][i]:
                return False
        row=(x//3)*3
        col=(y//3)*3
        for i in range(3):
            for j in range(3):
                if self.board[row+i][col+j]==n:
                    return False
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.board=board
        for x in range(9):
            for y in range(9):
                if board[x][y]=='.':
                    for n in range(1,10):
                        if self.isvalid(x,y,str(n)):
                            board[x][y]=str(n)
                            if self.isValidSudoku(board):
                                return True
                            board[x][y]='.'
                    return False
        return board
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.isValidSudoku(board)
        """
        Do not return anything, modify board in-place instead.
        """
      
    
        

        
        