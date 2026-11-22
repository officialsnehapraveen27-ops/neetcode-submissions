class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq_map=[0]*26

        n=len(s)
        m=len(t)

        if n!=m:
            return False

        i,j=0,0
        for i in range(n):

            freq_map[ord(s[i])-ord('a')]+=1

        
        for j in range(m):

            if freq_map[ord(t[j])-ord('a')]:
                
                freq_map[ord(t[j])-ord('a')]-=1
            
            

        
        for v in freq_map:

            if v <0 or v>0:

                return False
        
        return True

        
        