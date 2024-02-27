class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        i=missing=_range=0
        while _range<n:
            if i<len(nums) and nums[i]<=_range+1:
                _range+=nums[i]
                i+=1
            else:
                missing+=1
                _range+=_range+1
        return missing