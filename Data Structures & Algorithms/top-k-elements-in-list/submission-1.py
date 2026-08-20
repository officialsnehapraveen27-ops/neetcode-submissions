class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_dict={}
        n=len(nums)

        for num in nums:

            freq_dict[num]=freq_dict.get(num, 0)+1

        
        bucket_list = [[] for i in range(n+1)]

        for key,value in freq_dict.items():

            bucket_list[value].append(key)

        result=[]

        for i in range(n,0, -1):

            if bucket_list[i]:

                for num in bucket_list[i]:
                    result.append(num)

                    if len(result)==k:

                        return result

        return 