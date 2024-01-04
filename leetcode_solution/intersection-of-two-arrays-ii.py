class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=list(set(nums1) & set(nums2))
        
        mp1=Counter(nums1)
        mp2=Counter(nums2)
        print(mp1)
        ans=[]
        for el in l:
            mi=min(mp1[el],mp2[el])
            for i in range(mi):
                ans.append(el)
        print(ans)
        return ans
        
        