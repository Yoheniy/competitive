class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d={}
        
        
        for el in paths:
            dirhold=el.split(" ")
            for i in range(1,len(dirhold)):
                start=dirhold[i]
                want1=start.find("(")+1
                want2=start.find(")")
                dirtxt=start[want1:want2]
                dot=start.find(".")
                dirval=start[:dot]
                root=list(dirhold[0])
                root.append("/")
                root.append(dirval)
                root.append(".txt")
                rootString="".join(root)
                if dirtxt not in d:
                    d[dirtxt]=[rootString]
                else:
                    d[dirtxt].append(rootString)
            
                

           
            ans=list(d.values())
            

       
        return [el for el in ans if len(el)>1]
            


                


        
        