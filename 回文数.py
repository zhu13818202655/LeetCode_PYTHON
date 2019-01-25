'''Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

