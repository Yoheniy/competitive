class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff=float("inf")
        ans=0
        for i in range(len(nums)):
            l=i+1
            r=len(nums)-1
            while l<r:
                threesum=nums[i]+nums[l]+nums[r]
                if threesum>target:
                    r-=1


                elif threesum<target:
                    l+=1
                else:
                    return threesum
                if diff>abs(target-threesum):
                    diff=abs(target-threesum)
                    ans=threesum
        return ans

        return ans 
                
        