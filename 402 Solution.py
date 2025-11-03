class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        target = len(num) - k

        for i, digit in enumerate(num):
            remaining = len(num) - i - 1
            while stack and digit < stack[-1] and len(stack) + remaining >= target:
                stack.pop()
            if len(stack) < target:
                stack.append(digit)

        # Remove leading zeros
        result = ''.join(stack).lstrip('0')
        return result if result else "0"
