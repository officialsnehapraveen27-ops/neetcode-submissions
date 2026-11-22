class Solution:
    def isValid(self, s: str) -> bool:


        bracket={'[':']','{':'}','(':')'}

        stack=[]*len(s)
        if len(s) <=1:
            return False

        for b in s:

            if b in bracket.keys():

                stack.append(b)

            elif b in bracket.values():

                if stack and bracket[stack[-1]] == b:

                    stack.pop()
                
                else:

                    return False
        
        if len(stack)==0:

            return True
        else: 
            return False



        