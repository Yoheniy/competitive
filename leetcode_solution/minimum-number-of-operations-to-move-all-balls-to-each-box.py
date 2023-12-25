class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l=[]
        
        for i in range(len(boxes)):
            cn=0
            for j in range(len(boxes)):
                if boxes[j]=='1':
                    cn+=abs(j-i)
            l.append(cn)
        return l
                

        