class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


        freq_map={}

        for num in nums:

            if num in freq_map:

                freq_map[num]+=1
                return True
            
            freq_map[num]=1

        return False

        