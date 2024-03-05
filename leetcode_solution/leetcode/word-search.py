class Solution:
    def __init__(self):
        self.ceil=[]
        self.visited=set()
        self.letter=""
    def dfs(self,letter,x,y):
        if not letter:
            return True
        if not (0<=x<len(self.ceil) and 0<=y<len(self.ceil[0])):
            return False
        if (x,y) in self.visited or letter[0]!=self.ceil[x][y]:
            return False
        self.visited.add((x,y))
        letter=letter[1:]
        res=(
            self.dfs(letter,x+1,y) or
            self.dfs(letter,x-1,y) or
            self.dfs(letter,x,y+1) or 
            self.dfs(letter,x,y-1)
        )
        self.visited.remove((x,y))
        return res
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.ceil=board.copy()
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y]==word[0]:
                    if  self.dfs(word,x,y):
                        return True
        return False
        