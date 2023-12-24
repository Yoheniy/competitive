class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        d=""
        for i in range(len(strs[0])):
            if strs[0][i]==strs[len(strs)-1][i]:
                d+=strs[0][i]
            else:
                break
        return d
                    

        
        
        