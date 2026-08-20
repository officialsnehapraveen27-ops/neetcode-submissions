class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        freq_map={}

        for let in s:

            if let not in freq_map:

                freq_map[let]=1
            else:

                freq_map[let]+=1
        

        for let in t:

            if let in freq_map:

                freq_map[let]-=1
            
            else:

                return False

        
        for value in freq_map.values():

            if value!=0:

                return False
        
        return True
        