class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)

        largest=1

        if not nums:

            return 0

        for num in numSet:

            #start with the first number of the sequence

            if num - 1 not in numSet:

                current=1

                while num + 1 in numSet:

                    current+=1
                    num+=1
                
            
                largest=max(largest,current)
        
        return largest