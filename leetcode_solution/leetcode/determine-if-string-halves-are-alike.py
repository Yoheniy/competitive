class Solution:
    def halvesAreAlike(self, s: str) -> bool:
    
        l=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        cnl,cnr=0,0
  
        h=Counter(s[:(len(s)//2)])
        f=Counter(s[len(s)//2:])
        print(h,f)

        for i in range(len(l)):
            if l[i] in h and l[i] in f:
                cnl+=h[l[i]]
                cnr+=f[l[i]]
            elif l[i] in f:
                cnr+=f[l[i]]
            elif l[i] in h:
                cnl+=h[l[i]]
        print(cnl,cnr)
        if cnl==cnr:
            return True
        return False