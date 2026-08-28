class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        import math
        operators={'+','-','*','/'}
        operands=[]
        for char in tokens:
            if char not in operators:
                operands.append(int(char))
            else:
                operand2=operands.pop()
                operand1=operands.pop()
                if char=='+':
                    operands.append(operand1+operand2)
                elif char=='-':
                    operands.append(operand1-operand2)
                elif char=='*':
                    operands.append(operand1*operand2)
                elif char=='/':
                    if (operand2<0 or operand1<0) and operand1*operand2<0:
                        operands.append(math.ceil(operand1/operand2))
                    else:
                        operands.append(operand1//operand2)
        return operands[0]
        # for i in range(len(tokens)):
        #     if i==0:
        #         operand1=int(tokens[i])
        #         continue
        #     elif i%2==1:
        #         operand2=int(tokens[i])
        #     else:
        #         if tokens[i]=='+':
        #             result=operand1+operand2
        #             operand1=result
        #         elif tokens[i]=='-':
        #             result=operand1-operand2
        #             operand1=result
        #         elif tokens[i]=='*':
        #             result=operand1*operand2
        #             operand1=result
        #         elif tokens[i]=='/':
        #             result=operand1//operand2
        #             operand1=result
        # return result