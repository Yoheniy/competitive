class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        num=list(s)
        num.sort()
        ma=1
        cn=1
        j=1
        if(len(num)==0):
            return 0
        while(j<len(num)):
            if(num[j]-num[j-1]!=1):
                cn=1
                j+=1
            else:
                cn+=1
                j+=1
                ma=max(ma,cn)
        return ma
       

        