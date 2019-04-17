class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            for temp in res:
                x = temp[:] #复制
                x.append(num)
                res.append(x)
        return res
nums = [1,2,3]
a = Solution().subsets(nums=nums)
print(a)