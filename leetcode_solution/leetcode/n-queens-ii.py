class Solution:
    def __init__(self):
        self.pos=set()
        self.neg=set()
        self.col=set()
        self.board=[]
        self.ans=0
    def dfs(self,row):
        if row>=len(self.board):
            self.ans+=1
            return
        for i in range(len(self.board[0])):
            if i in self.col or (row+i) in self.pos or (row-i) in self.neg:
                continue
            self.col.add(i)
            self.pos.add(row+i)
            self.neg.add(row-i)
            self.board[row][i]='Q'
            self.dfs(row+1)
            self.col.remove(i)
            self.pos.remove(row+i)
            self.neg.remove(row-i)
            self.board[row][i]='.'
    def totalNQueens(self, n: int) -> int:
        self.board=[['.' for _ in range(n)] for i in range(n)]
        self.dfs(0)
        return self.ans
        