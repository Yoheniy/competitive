class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        me=abs(target[0])
        me+=abs(target[1])
        for el in ghosts:
            sum1=0
            sum1+=abs(target[0]-el[0])
            sum1+=abs(target[1]-el[1])
            if sum1<=me:
                return False 
        return True

        
        