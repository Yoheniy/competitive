class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        count=defaultdict(int)
        count[0]=1
        ans=0
        prefixsum=0
        for i in nums:
            prefixsum+=i
            ans+=count[prefixsum-goal]
            count[prefixsum]+=1
        return ans