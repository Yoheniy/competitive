class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans=0
        l,r=0,0
        unique=defaultdict(int)
        while r<len(s):
            unique[s[r]]+=1
            while unique[s[r]]>1:
                unique[s[l]]-=1
                l+=1
            
            ans=max(ans,r-l+1)
            r+=1
        return ans

        