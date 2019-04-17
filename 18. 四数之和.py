'''
#两个循环加上一个左右指针查找
def fourSum(nums, target: int):
    length = len(nums)

    all = []
    nums = sorted(nums)
    for i in range(length-3):
        if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:#加速
            continue
        for j in range(i+1, length-2):
            if nums[i] + nums[j] + nums[-2] + nums[-1] < target:#加速
                continue
            left = j+1
            right = length-1
            while left < right:
                sum = nums[i]+nums[j]+nums[left]+nums[right]
                if sum == target:
                    all.append([nums[i],nums[j],nums[left],nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                elif sum < target:
                    left += 1
                else:
                    right -= 1
    #list去重
    allt = []
    for r in all:
        if r not in allt:
            allt.append(r)
    return allt


#2.
#第一个for循环，先求后2个值可能的取值的所有情况，并且把它们储存在一个字典里，以和作为键。
# 第二个for，我们遍历前2个值所可能取的各种值，算出和并且检查target - onesum是否在我们的字典里，如果在，就说明我们找到了一个解。
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = set()
        sumans = {}
        if len(nums) < 4:
            return []
        for i in range(2, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                onesum = nums[i] + nums[j]
                if onesum not in sumans:
                    sumans[onesum] = [(i, j)]
                else:
                    sumans[onesum].append((i, j))
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                onesum = nums[i] + nums[j]
                if target - onesum in sumans:
                    for k in sumans[target - onesum]:
                        if k[0] > j:
                            ans.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
        return [i for i in ans]
'''

#3.
#与1类似，但是四个指针限制，每个指针通过与自身前一个比较，一样就跳过
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        _4_sum_list = []
        nums.sort()
        if nums[-1]*4 < target:#最后四个小于目标值，为空
            return []
        for i in range(len(nums)-3):
            if nums[i]*4 > target:
                break
            if i == 0 or nums[i] != nums[i-1]:
                ele = nums[i]
                target_3_sum = target - ele
                if nums[-1]*3 < target_3_sum:
                    continue
                for j in range(i+1, len(nums)-2):
                    ele2 = nums[j]
                    if ele2*3 > target_3_sum:
                        break
                    if j==i+1 or ele2 != nums[j-1]:
                        target_2_sum = target_3_sum - ele2
                        point_left = j+1
                        point_right = len(nums)-1
                        while point_left < point_right:
                            if nums[point_left] + nums[point_right] > target_2_sum:
                                point_right -= 1
                            elif nums[point_left] + nums[point_right] < target_2_sum:
                                point_left += 1
                            else:
                                aaa = [ele, ele2,nums[point_left], nums[point_right]]
                                _4_sum_list.append(aaa)
                                point_left += 1
                                point_right -= 1
                                while point_left < point_right and nums[point_left] == nums[point_left-1]:
                                    point_left += 1
                                while point_left < point_right and nums[point_right] == nums[point_right+1]:
                                    point_right -= 1

        return _4_sum_list

