from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq_dict=defaultdict(list)
        result=[]
        for word in strs:
            freq_list=[0]*26
            for ch in word:

                freq_list[ord(ch)-ord('a')]+=1

            key=tuple(freq_list)
            freq_dict[key].append(word)
        

        for key,value in freq_dict.items():

            result.append(value)

        return result