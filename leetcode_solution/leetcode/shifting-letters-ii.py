class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ps=[0]*len(s)
        for i in range(len(shifts)):
            if shifts[i][2]==0:
                l=shifts[i][0]
                r=shifts[i][1]
                if r+1<len(s):
                    ps[l]+=-1
                    ps[r+1]+=1
                else:
                    ps[l]+=-1
            elif shifts[i][2]==1:
                l=shifts[i][0]
                r=shifts[i][1]
                if r+1<len(s):
                    ps[l]+=1
                    ps[r+1]-=1
                else:
                    ps[l]+=1
        psum=[]
        x=0
        for i in range(len(s)):
            x+=ps[i]
            psum.append(x)
        print(psum)
        ans=[]
        for i in range(len(s)):
            ans.append(((ord(s[i])-ord('a')+psum[i])%26)+ord('a'))
        print(ans)
        ans=[chr(x) for x in ans]

        return "".join(ans)