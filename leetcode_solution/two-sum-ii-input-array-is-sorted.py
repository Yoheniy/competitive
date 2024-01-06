class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans=[]
        left,right=0,len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]==target:
                ans.append(left+1)
                ans.append(right+1)
                return ans
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                right-=1
        