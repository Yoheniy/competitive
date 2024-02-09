class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq=[0]*(len(nums))
        for req in requests:
            l=req[0]
            r=req[1]
            if r+1<len(nums):
                freq[l]+=1
                freq[r+1]-=1
            else:
                freq[l]+=1
        
        for i in range(1,len(freq)):
            freq[i]=freq[i-1]+freq[i]
        
        
        freq.sort(reverse=True)
        nums.sort(reverse=True)
        print(freq,nums)
        ans=0
        mod=10**9 + 7
        for i in range(len(freq)):
            ans+=(nums[i]*freq[i])
        return ans%mod

            

        