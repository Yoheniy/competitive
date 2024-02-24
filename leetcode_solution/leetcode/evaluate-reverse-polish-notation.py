class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=['+', '-', '*','/']
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                operand2=stack.pop()
                operand1=stack.pop()
                if tokens[i]=='*':
                    stack.append(operand1*operand2)
                elif tokens[i]=='+':
                    stack.append(operand1+operand2)
                elif tokens[i]=='-':
                    stack.append(operand1-operand2)
                else:
                    temp=int(operand1/operand2)
                    stack.append(temp)
        return stack[-1]
        