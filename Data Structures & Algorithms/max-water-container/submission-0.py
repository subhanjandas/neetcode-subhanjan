class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area, l, r = 0, 0, n - 1

        # Area = Width * Height
        # Width = heights[r] - heights[l]
        # Height = min(heights[r], heights[l])

        # Move the pointer inwards which is shorter in height

        while l < r:
            curr_area = (r - l) * min(heights[l], heights[r])

            if l >= r:
                r -= 1
            else:
                l += 1

            max_area = max(max_area, curr_area) 

        return max_area