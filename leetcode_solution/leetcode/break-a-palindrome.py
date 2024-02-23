class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        lis=list(palindrome)
        right=len(palindrome)-1
        left=0
        if len(palindrome)<=1:
            return ""
        while left<right:
            if lis[left]==lis[right] and lis[left]!='a':
                lis[left]='a'
                break
            left+=1
            right-=1
        if lis==lis[::-1]:
            lis[-1]='b'
        return "".join(lis)
                
             

        