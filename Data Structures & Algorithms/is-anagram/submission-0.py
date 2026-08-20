class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        s1={}
        t1={}

        if len(s)!= len(t):

            return False

        for i in range(len(s)):

            if s[i] in s1 :

                s1[s[i]] +=1
            else:
                s1[s[i]] = 1

            
        for j in range(len(t)):

            if t[j] in t1:

                t1[t[j]]+=1

            else:
                 t1[t[j]] =1
        

        if s1 == t1 : 

            return True
        
        else: 

            return False
        