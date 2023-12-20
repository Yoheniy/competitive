class Solution:
    def interpret(self, command: str) -> str:
        s=""
        for i in range(len(command)):
            if(command[i]=='('and command[i+1]==')'):
                s+="o"
                
            elif(command[i]=='('and command[i+1]=='a'):
                s+="al"
               
            elif(command[i]=='G'):
                s=s+"G"
        return s

        