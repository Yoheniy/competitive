class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        m={}
        i=0
        arr=[]
        for i in range(len(intervals)):
            m[intervals[i][0]]=i
            arr.append(intervals[i][0])
            i+=1
        arr.sort()
        ans=[-1]*len(intervals)
        for i in range(len(intervals)):
            temp=bisect.bisect_left(arr,intervals[i][1])
            if temp>=len(arr):
                continue
            ans[i]=m[arr[temp]]
        return ans
        
        
        
        
        
        
        
        

