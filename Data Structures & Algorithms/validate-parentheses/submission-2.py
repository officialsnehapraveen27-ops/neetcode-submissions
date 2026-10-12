class Solution:
    def isValid(self, s: str) -> bool:

        brackets={'(':')','[':']','{':'}'}

        stack=[]


        for character in s:

            if character in brackets.keys():

                stack.append(character)
            
            else: 


                if len(stack) > 0:

                    if brackets[stack[-1]] == character:

                        stack.pop()

                    else:

                        return False

                
                elif len(stack)==0:

                    if character in brackets.values():

                        return False
                    

                    
      
        
        return len(stack)==0




        