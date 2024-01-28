class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix=[0]*len(nums)
        prefix[0]=nums[0]
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]+nums[i]
        print(prefix)
        m=defaultdict(int)
        m[0]=1
        ans=0
        for el in prefix:
            if el-k in m:
                ans+=m[el-k]
            m[el]+=1
        return ans




        