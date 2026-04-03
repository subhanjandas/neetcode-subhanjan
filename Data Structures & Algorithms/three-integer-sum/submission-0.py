class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range (n):
            if i > 0 and nums[i] == nums[i-1]: 
                continue
            j = i+1
            k = n-1
            target = -nums[i]
            while j < k:
                curr_sum = nums[j] + nums[k]
                if curr_sum > target:
                    k -= 1
                elif curr_sum < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]: 
                        j += 1
        return res    
