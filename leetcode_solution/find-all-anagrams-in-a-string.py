class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''ans = []
        if len(s)<len(p):
            return ans
        
        palp = [0]*26
        for c in p:
            palp[ord(c)-97]+=1
        
        win = len(p)

        salp = [0]*26
        
        for i in range(len(s)):
            salp[ord(s[i])-97]+=1
            if (i>=win):
                salp[ord(s[i-win])-97]-=1
            if (salp==palp):
                ans.append(i-win+1)
            
                
        return ans'''
        pcounter=Counter(p)
        scounter=Counter()
        left=0
        ans=[]
        for right in range(len(s)):
            scounter[s[right]]+=1
            while right-left>=len(p):
                scounter[s[left]]-=1
                left+=1
            if scounter==pcounter:
                ans.append(left)
        return ans



        