class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans=curr=0
        m={0:1}
        for num in nums:
            curr+=num
            key=curr%k
            if key in m:
                ans+=m[key]
                m[key]+=1
            else:
                m[key]=1
        return ans 
        