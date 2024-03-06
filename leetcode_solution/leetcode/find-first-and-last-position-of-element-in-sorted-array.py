class Solution:
    def __init__(self):
        self.searchleft
        self.searchright
    def searchleft(self,nums,target):
        left,right=0,len(nums)-1
        indx=-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                indx= mid
            if nums[mid]>=target:
                right=mid-1
            else:
                left=mid+1
        return indx
    def searchright(self,nums,target):
        left,right=0,len(nums)-1
        indx=-1
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                indx= mid
            if nums[mid]<=target:
                left=mid+1
            else:
                right=mid-1
        return indx
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.searchleft(nums,target),self.searchright(nums,target)]
        