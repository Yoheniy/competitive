class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1="qwertyuiopQWERTYUIOP"
        row2="asdfghjklASDFGHJKL"
        row3="zxcvbnmZXCVBNM"
        l=[]
        d1={el:0 for el in row1}
        d2={el:1 for el in row2}
        d3={el:2 for el in row3}
        d=d1.copy()
        d.update(d2)
        d.update(d3)
        for word in words:
            
            temp=d[word[0]]
            if all(d[char]==temp for char in word):
                l.append(word)
        
        
        return l

        
                

                       
                    
                    





      