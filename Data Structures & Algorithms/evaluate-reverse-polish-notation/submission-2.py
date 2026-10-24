class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]

        for t in tokens:

            if t.lstrip("-").isdigit():

                stack.append(int(t))

            else:
                
                
                num2=stack.pop()
                num1=stack.pop()
                    

                if t == "+":

                    total=num1+num2

                    stack.append(total)

                elif t == "-":

                    res = num1 - num2

                    stack.append(res)

                elif t == "*":

                    res = num1*num2

                    stack.append(res)

                elif t=="/":

                    if num2!=0:

                        res = int( num1/num2)
                        stack.append(res)

        
        return stack.pop()







        