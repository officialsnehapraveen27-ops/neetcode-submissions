class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freqs={}

        for char in s:

            freqs[char]=freqs.get(char,0)+1
        
        for char in t:

            if char in freqs:

                freqs[char]-=1
            else:

                return False
        
        for k,v in freqs.items():

            if v < 0 or v > 0:
                return False

        return True
        