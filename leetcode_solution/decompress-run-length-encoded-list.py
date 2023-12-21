class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(1,len(nums),2):
            j=i-1
            for k in range(nums[j]):
                l.append(nums[i])
        return l

        