class Solution:

    def util(self, left, right):
        if left == right:
            return left
        if left-right == -1:
            return left & right
        i = 1
        included_2_pows = []
        while i <= right:
            if i >= left:
                if included_2_pows:
                    return 0
                included_2_pows.append(i)
            i *= 2
        if included_2_pows and left < included_2_pows[0]:
            return 0
        if not included_2_pows:
            included_2_pows.append(i//2)
        return included_2_pows[0] + self.util(left - included_2_pows[0], right - included_2_pows[0])

    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        return self.util(left, right)
