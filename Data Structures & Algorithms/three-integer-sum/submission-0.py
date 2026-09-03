class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        triplets = set()
        n=len(nums)

        nums.sort()

        if not nums or n < 3 or nums[0] >1:

            return []

        for i in range(n-2):

            left=i+1
            right=n-1

            while left < right:
                sum= nums[i]+nums[left]+nums[right]

                if sum == 0:

                    triplet=tuple([nums[i],nums[left],nums[right]])
                    triplets.add(triplet)

                    left+=1
                    right-=1

                elif sum > 0:

                    right-=1

                elif sum <0:
                    left+=1

        return [ list(triplet)  for triplet in triplets]
        