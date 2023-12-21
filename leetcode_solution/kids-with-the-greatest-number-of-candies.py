class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        l=sorted(candies)
        ls=[]
        for i in range(len(candies)):
            if((candies[i]+extraCandies)>=l[len(l)-1]):
                ls.append(True)
            else:
                ls.append(False)
        return ls
        