class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        k,i=0,1
        checkincr,checkdec=0,0

        if len(arr)<3:
            return False
    
        while i<len(arr) and arr[i-1]<arr[i]:
            k+=1
            i+=1
            checkincr=1
        while i<len(arr) and arr[k]>arr[i]:
            i+=1
            k+=1
            checkdec=1
        return i==len(arr) and checkincr==1 and checkdec==1
            
        
        