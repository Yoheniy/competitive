class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        map1=Counter(p)
        l,r=0,0
        ans=[]
        while r<len(s):
            
            temp=s[l:r+len(p)]
            map2=Counter(temp)
            print(map2)
            if map1==map2:
                ans.append(l)
                
            r+=1
            l+=1

            
        
        return ans
        