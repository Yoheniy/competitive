class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        l=num//3
        r=[]
        if((l+(l+1)+(l+2))==num):
            r.append(l)
            r.append(l+1)
            r.append(l+2)
            return r
        elif((l+(l-1)+(l+1))==num):
            r.append(l-1)
            r.append(l)
            r.append(l+1)
            return r
        elif((l+(l-1)+(l-2))==num):
            r.append(l-2)
            r.append(l-1)
            r.append(l)
            return r
        else:
            return r





        