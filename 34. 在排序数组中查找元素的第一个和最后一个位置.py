class Solution:
    def searchRange(self, nums, target: int):
        try:
            a = nums.index(target)
        except ValueError as e:
            a = -1
            nums.reverse()
        try:
            b = len(nums)-nums.index(target)-1
        except ValueError as e:
            b = -1
            return [a,b]
a = [1,2,3,6,6,9,8,45,6,59,85]
target = 98
result = Solution().searchRange(nums=a,target=target)
print(result)