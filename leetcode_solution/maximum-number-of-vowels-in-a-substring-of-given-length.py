class Solution:
    
    def maxVowels(self, s: str, k: int) -> int:
        def is_vowel(char):
            return char in "aeiou"
        left=0
        cnvowel=0
        ans=0
        for right in range(len(s)):
            if is_vowel(s[right]):
                cnvowel+=1
            while right-left>=k:
                if is_vowel(s[left]):
                    cnvowel-=1
                left+=1
            ans=max(ans,cnvowel)
        return ans
        