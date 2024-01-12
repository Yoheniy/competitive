class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=[]
        n=len(nums)
        
        for i in range(n):
            l,r=i+1,n-1
            #if the element at the begining is repeated we have to re
            if i>0 and nums[i]==nums[i-1]:
                continue
            while l<r:
                threesum=nums[i]+nums[l]+nums[r]
                if threesum==0:
                    ans.append([nums[i],nums[l],nums[r]])
                    
                    l+=1
                    #r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif threesum>0:
                    r-=1
                else:
                    l+=1

        return ans
                

                        

        