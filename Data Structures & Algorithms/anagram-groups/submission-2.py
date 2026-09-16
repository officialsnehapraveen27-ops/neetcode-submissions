from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq_dict=defaultdict(list)
        result=[]
        for word in strs:

            key= tuple(sorted(word))
            
            freq_dict[key].append(word)
        

        for key,value in freq_dict.items():

            result.append(value)

        return result