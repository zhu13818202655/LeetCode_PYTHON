'''给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。'''

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left = 0
    right = len(height)-1
    maxarea = 0
    while left < right:
        h = min(height[left],height[right])
        maxarea = max(maxarea,h*(right-left))
        if height[left]<height[right]:
            left += 1
        else:
            right -= 1
    return maxarea

print(maxArea([1,3,9,5,89,26,57,5,4,6,8,9,25]))