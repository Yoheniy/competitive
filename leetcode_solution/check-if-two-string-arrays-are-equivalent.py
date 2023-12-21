class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1=""
        s2=""
        for word11 in word1:
            for i in word11:
                s1+=i
        for word12 in word2:
            for i in word12:
                s2+=i
        if(s1==s2):
            return True
        return False
        