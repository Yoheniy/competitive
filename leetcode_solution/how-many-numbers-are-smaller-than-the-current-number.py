class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        temp=sorted(nums)
              
        for el in nums:
            ans.append(temp.index(el))
        return ans

            



        