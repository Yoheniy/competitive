class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={"2":['a','b','c'],
             "3":['d','e','f'],
             "4":['g','h','i'],
             "5":['j','k','l'],
             "6":['m','n','o'],
             "7":['p','q','r','s'],
             "8":['t','u','v'],
             "9":['w','x','y','z']
            }
    
        ans=[]
        def solve(p,level):
            if len(p)==len(digits):
                ans.append("".join(p))
                return 
            temp=dic[digits[level]]
            for i in range(len(temp)):
                p.append(temp[i])
                solve(p,level+1)
                p.pop()
            return ans
        return solve([],0)
            