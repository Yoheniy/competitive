class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        stack2=[]
        openp=['(','[','{']
        closep=[')',']','}']
        if s[0] in closep:
            return False
        for i in range(len(s)):
            
            if s[i] in openp:
                stack.append(s[i])
            else:
                stack2.append(s[i])
                if stack and s[i]==']' and stack[-1]=='[':
                    stack.pop()
                    stack2.pop()
                elif stack and s[i]==')' and stack[-1]=='(':
                    stack.pop()
                    stack2.pop()
                elif stack and s[i]=='}' and stack[-1]=='{':
                    stack.pop()
                    stack2.pop()
        return not stack and not stack2

        