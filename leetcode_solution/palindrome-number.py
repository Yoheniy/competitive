class Solution:
    def isPalindrome(self, x: int) -> bool:
        l=str(x)
        f=""
        for i in range(len(l)-1,0,-1):
            f=f+l[i]
        f=f+l[0]
        if(f==l):
            return True
        else:
            return False

    

        