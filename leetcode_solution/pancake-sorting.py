class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n=len(arr)
        ans=[]
        for i in range(n):
            j=max(arr[:n])
            indx=arr.index(j)
            arr=arr[:indx+1][::-1]+arr[indx+1:]
            arr=arr[:n][::-1]
            
            ans.append(indx+1)
            ans.append(n)
            n-=1
        return ans





            
            




            

        