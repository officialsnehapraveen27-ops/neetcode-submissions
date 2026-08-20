from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict=defaultdict(list)

        for word in strs:

            char_freq=[0]*26

            for let in word:

                char_freq[ord(let)-ord('a')]+=1
            
            dict_key=tuple(char_freq)

            anagram_dict[dict_key].append(word)

        return list(anagram_dict.values())



        
        