class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l=list(set(nums1)&set(nums2))
        if len(l)==0:
            return -1

        return min(l)
        