class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lpivot=[]
        gpivot=[]
        epivot=[]
        for i in range(len(nums)):
            if(nums[i]<pivot):
                lpivot.append(nums[i])
            elif(nums[i]>pivot):
                gpivot.append(nums[i])
            else:
                epivot.append(nums[i])
        l=[]+lpivot+epivot+gpivot
        return l        
        