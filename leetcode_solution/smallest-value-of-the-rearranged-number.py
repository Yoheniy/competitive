class Solution:
    def smallestNumber(self, num: int) -> int:
        ans=""
        if num<0:
            s=str(num)
            l=[int(x) for x in s[1:] ]
            l.sort(reverse=True)
            print(l)
            ans="-"
            ans+="".join(str(x) for x in l)
            print(ans)

            return int(ans)
        else:
            s=str(num)
            l=[int(x) for x in s ]
            l.sort()
 
            if l[0]!=0:
                ans="".join(str(x) for x in l)
                return int(ans)
            else:
                for el in l:
                    if el!=0:
                        ans+=str(el)
                        l.remove(el)
                        break
                    
                
                ans+="".join(str(x) for x in l)
                return int(ans)
            



        