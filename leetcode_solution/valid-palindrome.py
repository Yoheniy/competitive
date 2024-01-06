class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        ans=[]
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                temp=s[i]
                t=temp.lower()
                ans.append(t)
        
        rans=ans[::-1]
        return rans==ans

        

        