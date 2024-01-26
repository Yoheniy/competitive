class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l=0
        ans=1
        m=Counter()
        for r in range(len(fruits)):
            m[fruits[r]]+=1
            while len(m)>2:
                m[fruits[l]]-=1
                if m[fruits[l]]==0:
                    del m[fruits[l]]
                l+=1
            if len(m)<=2:
                ans=max(ans,r-l+1)
        return ans


        '''        C=Counter()
        left=0
        max_len=0
        for right in range(len(fruits)):
            C[fruits[right]]+=1
            while(len(C)>2):
                C[fruits[left]]-=1
                if C[fruits[left]]==0:
                    del C[fruits[left]]
                left+=1
            max_len=max(max_len,right-left+1)
        return max_len'''



          

        