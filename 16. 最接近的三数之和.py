class Solution:#首先排序，运用两个循环，第一：遍历数组，第二：两个左右指针寻找最小差
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        length = len(nums)
        if length < 3:
            return False
        if length == 3:
            return nums[0]+nums[1]+nums[2]
        minn = 12365
        last = nums[0]
        for i in range(length-2):
            left = i+1
            right = length-1
            while left<right:
                sum = nums[i] + nums[left] +nums[right]
                if sum == target:
                    return target


                elif sum < target:
                    if abs(target-sum)<minn:
                        minn = abs(target-sum)
                        last = sum
                    left += 1
                else:
                    if abs(target-sum)<minn:
                        minn = abs(target-sum)
                        last = sum
                    right -= 1

        return last


