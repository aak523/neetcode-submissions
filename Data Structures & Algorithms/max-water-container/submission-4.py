class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water = 0
        l, r = 0, len(heights) - 1
        while l < r:
            max_water = max(
                max_water,
                self.water(l, r, heights[l], heights[r])   
            )
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max_water
        
    def water(self, l: int, r: int, l_height: int, r_height: int):
        return min(l_height, r_height) * (r - l)