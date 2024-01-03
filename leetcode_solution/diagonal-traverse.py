class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diag=[]
        m=len(mat)
        n=len(mat[0])
        for k in range(m):
            i=k
            j=0
            temp=[]

            while i>=0 and j<n:
 
                temp.append(mat[i][j])
                i=i-1
                j=j+1

            diag.append(temp)
           

        for k in range(1,n):
            i=m-1
            j=k
            temp=[]

            while j<n and i>=0:
                temp.append(mat[i][j])
                i=i-1
                j=j+1
            diag.append(temp)
        c=0
        for el in diag:
            if c%2!=0:
                el.reverse()
                c+=1
            else:
                c+=1
                continue
        l=[item for sublist in diag for item in sublist]
        return l
            