class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n=len(nums)
        bucket=[[] for i in range(n+1)]

        freq_map={}

        for num in nums:

            freq_map[num]=freq_map.get(num,0)+1

        for num,freq in freq_map.items():

            bucket[freq].append(num)

        result=[]
        for i in range(n,-1,-1):
            
            for num in bucket[i]:
                

                result.append(num)
                if len(result) ==k:
                    return result




            






        