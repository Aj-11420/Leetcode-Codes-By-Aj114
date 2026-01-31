class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        MIN_INT = -2147483648
        MAX_INT = 2147483647
        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_num = 0
        while x != 0:
            digit = x % 10
            x //= 10
            reversed_num = (reversed_num * 10) + digit
        result = sign * reversed_num
        if result < MIN_INT or result > MAX_INT:
            return 0
        return result
