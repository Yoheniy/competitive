class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        map=Counter(nums)
        del map[nums[0]]
        n=len(nums)-map[nums[0]]
        ans=0
        mult=1
        for el in map.values():
            ans+=mult*el
    
            mult+=1

        print(map)
        return ans 
    
    
        

        




        