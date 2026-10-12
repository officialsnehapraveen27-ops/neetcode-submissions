class Solution:
    def isValid(self, s: str) -> bool:

        brackets={'(':')','[':']','{':'}'}

        stack=[]

        
        for character in s:

            if character in brackets:

                stack.append(character)

            else:

                if not stack or brackets[stack[-1]] != character:

                    return False

                else:

                    stack.pop()


        return len(stack)==0

        




        