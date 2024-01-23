class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res=0
        l=[]
        prevsum=defaultdict(lambda:0)
        cursum=0
        for el in nums:
            if el%2!=0:
                l.append('1')
            else:
                l.append('0')
        l=[int(x) for x in l]
        for i in range(len(nums)):
            cursum+=l[i]
            if cursum==k:
                res+=1
            if cursum-k in prevsum:
                res+=prevsum[cursum-k]
            prevsum[cursum]+=1
      
        return res