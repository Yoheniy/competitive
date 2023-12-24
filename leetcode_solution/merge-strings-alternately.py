class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        d=""
        l1=len(word1)
        l2=len(word2)
        mn=max(l1,l2)
        for i in range(mn):
            if(i<l1 and i<l2):
                d+=word1[i]
                d+=word2[i]
            elif(i<l1 and i>=l2):
                d+=word1[i]
            elif(i>=l1 and i<l2):
                d+=word2[i]
            else:
                continue
        return d            
            
        