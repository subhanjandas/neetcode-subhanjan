class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lp = 0
        rp = n-1
        res = [0] * n
        resp = n-1
        while lp <= rp:
            if abs(nums[lp]) > abs(nums[rp]):
                res[resp] = nums[lp] ** 2
                lp += 1
            else:
                res[resp] = nums[rp] ** 2
                rp -= 1
            resp -= 1
        return res