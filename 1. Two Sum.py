#1.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for a in nums:
            start = nums.index(a) #这边不用担心如果a出现两次，索引值会出错，因为第一个a不行，那么第二个a也不行
            nextindex = start + 1
            newnums = nums[nextindex:]
            if (target - a) in newnums:
                return [nums.index(a), nextindex + newnums.index(target - a)]


#2.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if target-nums[i] not in dict:
                dict[nums[i]]=i
            else:
                return [dict[target-nums[i]],i]


#3.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,value in enumerate(nums):
            p = target-value
            if p in nums:
                p_index = nums.index(p)
                if p_index != i:
                    return [i, p_index]
