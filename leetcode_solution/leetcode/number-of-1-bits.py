class Solution:
    def hammingWeight(self, n: int) -> int:
        #to convert from number to binasry we can use ->bin(number)
        s=bin(n)
        c=s.count('1')
        return c
        