class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rp, wp, n = 0, 0, len(nums)

        for rp in range(n):
            if nums[rp] != 0:
                nums[rp], nums[wp] = nums[wp], nums[rp]
                rp += 1
                wp += 1
            else:
                rp += 1
                
        