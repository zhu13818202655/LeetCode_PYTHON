class Solution:
    def search(self, nums, target: int) -> int:
        try:
            a = nums.index(target)
            return a
        except ValueError:
            return -1
nums = [1,2,3,6,9,14,56]
target = 19
a = Solution().search(nums,target)
print(a)