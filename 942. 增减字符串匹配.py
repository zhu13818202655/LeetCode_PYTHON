class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        temp = [i for i in range(len(S)+1)]
        left = 0
        right = len(temp) - 1
        for key in S:
            if key == 'I':
                res.append(left)
                left+=1
            else:
                res.append(right)
                right-=1
        res.append(max(right,left))
        return res
