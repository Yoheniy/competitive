class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        l,r=0,10
        ans=[]

        m=defaultdict(int)
        while r<=len(s):
            temp=s[l:r]
            m[temp]+=1
            l+=1
            r+=1
        for key,val in m.items():
            if val>=2:
                ans.append(key)

        return ans
