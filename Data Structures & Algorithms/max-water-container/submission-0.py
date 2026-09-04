class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area=0

        i,j=0,len(heights)-1

        if not heights:

            return 0

        while i < j:

            area=(j-i) * min(heights[i],heights[j])

            max_area= max(max_area,area)

            if heights[i] > heights[j]:

                j-=1
            elif heights[j] >= heights[i]:

                i+=1
        return max_area
        