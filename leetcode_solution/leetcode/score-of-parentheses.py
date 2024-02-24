class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans=count=0
        for i in range(len(s)):
            if s[i]=='(':
                count+=1
            else:
                count-=1
                if s[i-1]=='(':
                    ans+=1<<count
        return ans 

        