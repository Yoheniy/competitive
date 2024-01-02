class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        reverse=[[0]*len(image) for i in range(len(image[0]))]
        k=0
        for i in range(len(image)):
            # reverse[i]=revers
            for j in range(len(image[0])-1,-1,-1):
                reverse[i][k]=image[i][j]
                k+=1
            k=0
        for i in range(len(reverse)):
            # reverse[i]=revers
            for j in range(len(reverse[0])):
                reverse[i][j]=1-reverse[i][j]
        return reverse
        
            
        