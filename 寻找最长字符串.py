class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        u = ''
        for i in range(len(s)):
            k = s[i]
            if k not in u:
                u+=k
                res = max(len(u),res)
            else:
                index = u.find(k)
                u = u[index+1:]+k
        return res