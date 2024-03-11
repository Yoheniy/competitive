class Solution:
    def firstUniqChar(self, s: str) -> int:
        c=Counter(s)
        m=defaultdict(int)
        for i in range(len(s)):
            if c[s[i]] not in m:
                m[c[s[i]]]=i
        if 1 in m.keys():
            return m[1]
        return -1
        
            

        