class Solution:
    def trap(self, height: List[int]) -> int:

        n=len(height)
        leftMax = height[0]
        rightMax = height[n-1]

        l,r=1,n-2
        total=0

        if not height or n <3:

            return 0
        while l<= r:

            if leftMax <= rightMax:

                if leftMax-height[l] >= 0:
                    total+= leftMax - height[l]
                
                leftMax=max(height[l],leftMax)

                l+=1

            else:

                if rightMax - height[r] > 0:
                    total+= rightMax- height[r]
                

                rightMax=max(rightMax,height[r])

                r-=1

        return total



        