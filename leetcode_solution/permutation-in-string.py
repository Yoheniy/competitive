class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1counter=Counter(s1)
        s2counter=Counter()
        left=0
        k=len(s1)
        for right in range(len(s2)):
            s2counter[s2[right]]+=1
            while right-left>=k:
                s2counter[s2[left]]-=1
                left+=1
            if s1counter==s2counter:
                return True
        return False


        return s1counter-s2counter==Counter()
        