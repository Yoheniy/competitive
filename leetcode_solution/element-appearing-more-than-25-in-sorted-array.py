class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        mult=100/len(arr)
        l=list(set(arr))
        for i in l:
            amount=arr.count(i)
            if(amount*mult>25):
                return i
        return 
        