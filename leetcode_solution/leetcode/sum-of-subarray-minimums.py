class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        ans=0
        mod = 10**9 + 7 
        prev_smaller=[i for i in range(len(arr))]
        next_smaller=[len(arr)-i-1 for i in range(len(arr))]
        stack=[]
        for i in range(len(arr)):
            while stack and arr[stack[-1]]>arr[i]:
                next_smaller[stack[-1]]=i-stack[-1]-1
                stack.pop()
            stack.append(i)
        stack.clear()      
        for i in range(len(arr)-1,-1,-1):
            while stack and arr[stack[-1]]>=arr[i]:
                prev_smaller[stack[-1]]=stack[-1]-i-1
                stack.pop()
            stack.append(i)
        for i in range(len(arr)):
            ans+=(((prev_smaller[i]+1)*(next_smaller[i]+1))*arr[i])
            ans%=mod
        return int(ans)

        