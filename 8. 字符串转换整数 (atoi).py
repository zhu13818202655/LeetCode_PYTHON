##常规操作
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if '' == str.strip():
            return 0
        sign, base, i = 1, 0, 0
        INT_MAX = 2147483647
        INT_MIN = -INT_MAX - 1
        while (str[i] == ' '):
            i += 1
        if str[i] == '-' or str[i] == '+':
            if str[i] == '-':
                sign = -1
            i += 1

        while i < len(str) and '0' <= str[i] <= '9':
            if base > INT_MAX // 10 or base == INT_MAX // 10 and int(str[i]) > 7:
                return INT_MAX if sign == 1 else INT_MIN

            base = 10 * base + int(str[i])
            i += 1

        return base * sign

##运用正则
class Solution2:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re

        pattern = r"[\s]*[+-]?[\d]+"#[\s]匹配任何空字符
        match = re.match(pattern, str)
        if match:
            res = int(match.group())

            if res > 2 ** 31 - 1:
                res = 2 ** 31 - 1
            if res < - 2 ** 31:
                res = - 2 ** 31
        else:
            res = 0
        return res

s = '   a+69s5sd'
a = Solution2().myAtoi(str=s)
print(a)