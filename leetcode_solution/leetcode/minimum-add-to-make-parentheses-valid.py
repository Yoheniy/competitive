class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        cn=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(s[i])
            elif not stack and s[i]==')':
                cn+=1
            elif stack and s[i]==')' and stack[-1]=='(':
                stack.pop()
        return cn+len(stack)
            
        