class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort()
        ans=""
        c=1
        while c>0:    
            c=0
            for i in range(1,len(nums)):
                t1=str(nums[i-1])+str(nums[i])
                t2=str(nums[i])+str(nums[i-1])
                if t1>t2:
                    c+=1
                    nums[i],nums[i-1]=nums[i-1],nums[i]
        nums.reverse()
        ans="".join([str(x) for x in nums])
        return str(int(ans))
        


    

 

        