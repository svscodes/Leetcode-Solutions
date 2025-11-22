#
# Problem: 42. Trapping Rain Water
# Difficulty: Hard
# Link: https://leetcode.com/problems/trapping-rain-water/
# Language: python3
# Date: 2025-11-22


class Solution:
    def trap(self, height: List[int]) -> int:
        # tCap = 0
        # leftMax = []
        # lMax = height[0]
        # for i in range(len(height)):
        #     lMax  = max(lMax, height[i])
        #     leftMax.append(lMax)
        
        # rightMax = []
        # rMax = height[-1]
        # for i in height[::-1]:
        #     rMax = max(rMax, i)
        #     rightMax.append(rMax)
        # rightMax = rightMax[::-1]

        # for i in range(len(height)):
        #     uCap = min(leftMax[i], rightMax[i]) - height[i]
        #     if uCap > 0:
        #         tCap += uCap

        # return tCap

        l = 0
        r = len(height) - 1
        tCap = 0
        lMax, rMax = height[l], height[r]

        while l < r:
            if lMax <= rMax:
                l += 1
                lMax = max(lMax, height[l])
                uCap = lMax - height[l]

            else:
                r -= 1
                rMax = max(rMax, height[r])
                uCap = rMax - height[r]
                
            tCap += uCap 

        return tCap

            
