from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        n=len(nums)
        bucket_list= [[] for i in range(0,n+1)]
        result=[]

        frequency_map={}

        for num in nums:

            frequency_map[num]=frequency_map.get(num,0)+1

        
        for key,value in frequency_map.items():

            bucket_list[value].append(key)
        

        for i in range(n,-1,-1):


            for num in bucket_list[i]:

                result.append(num)

                if len(result) ==k:
                    return result


            
            

            




        
        