class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        s1 = ('').join(s.strip(' '))

        s1=s1.lower()

        i=0
        j= len(s1)-1

        while i < j:

            if s1[i].isalnum() and s1[j].isalnum():
                
                if s1[i] == s1[j]:

                    i+=1
                    j-=1

                else: 

                    return False
            else:
                if not s1[i].isalnum():
                    i+=1
                if not s1[j].isalnum():
                    j-=1
        return True
