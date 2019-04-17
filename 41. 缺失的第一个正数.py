class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()
        length = len(nums)
        try:
            pos = nums.index(1)
            while True:
                if nums[pos+1]-nums[pos] == 1 or nums[pos+1]-nums[pos] == 0:
                    pos += 1
                    if pos+1 == length:
                        return nums[pos]+1
                    continue
                else:
                    return nums[pos]+1
        except ValueError:
            return 1
nums = [7,8,9,11,12]
result = Solution().firstMissingPositive(nums=nums)
print(result)