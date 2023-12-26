class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d={x:i for i,x in enumerate(nums)}
        for el in operations:
            indx=d.get(el[0],-1)
            if indx!=-1:
                nums[indx]=el[1]
                d[el[1]]=indx

        return nums
        