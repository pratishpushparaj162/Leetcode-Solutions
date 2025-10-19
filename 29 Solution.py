import math

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = 0
        if dividend < 0 and divisor < 0:
            res = math.floor(dividend / divisor)
        elif dividend < 0 or divisor < 0:
            res = math.ceil(dividend / divisor)
        else:
            res = math.floor(dividend / divisor)
        
        # Clamp result to 32-bit signed integer range
        if res > 2**31 - 1:
            return (2**31) - 1
        elif res < -2**31:
            return -2**31
        
        return res
