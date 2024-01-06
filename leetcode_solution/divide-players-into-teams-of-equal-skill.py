class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sum1=sum(skill)
        target=sum1/int((len(skill)//2))
        
        print(target)
        skill.sort()
        left,right=0,len(skill)-1
        ans=0
        cn=0
        while left<=right:
            if skill[left]+skill[right]==target:
                print(skill[left],skill[right])
                ans+=(skill[left]*skill[right])
                cn+=1
                left+=1
                right-=1
                
            elif skill[left]+skill[right]>target:
                right-=1
            else:
                left+=1
        if ans==0 or cn!=len(skill)/2:
            return -1
        return ans 
        