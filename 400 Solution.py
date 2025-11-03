class Solution:
    def findNthDigit(self, n: int) -> int:
        if n < 10:
            return n
        k = 1
        while n > 9 * (10 ** (k-1)) * k:
            n -= 9 * (10 ** (k-1)) * k
            k += 1

        target = (10 ** (k-1)) + ((n-1) // k)
        index = (n-1) % k
        return int(str(target)[index])
