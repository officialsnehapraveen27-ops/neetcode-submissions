class Solution:
    def isPalindrome(self, s: str) -> bool:

        

        i=0
        j=len(s)-1

        while i < j:

            while i < j and not isAlNum(s[i]):
                i+=1

            while j > i and not isAlNum(s[j]):

                j-=1
            
            if s[i].lower() == s[j].lower():

                i+=1
                j-=1
            else:
                return False

        return True    

def isAlNum(ch):

        if (ord('A') <= ord(ch) <= ord('Z') or ord('a') <= ord(ch) <= ord('z') or ord('0') <= ord(ch) <= ord('9')):

            return True
        
        return False
