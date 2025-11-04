class Solution(object):
    def superPow(self, a, b):
        c = 0
        c = int("".join(map(str, b))) 
        return pow(a, c, 1337)  
