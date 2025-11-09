class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        left = iter(map(int, version1.split('.')))
        right = iter(map(int, version2.split('.')))

        left_end = False
        right_end = False
        while True:
            try: nl = next(left)
            except: left_end = True

            try: nr = next(right)
            except: right_end = True
            
            if not left_end or not right_end:
                if left_end: nl = 0
                if right_end: nr = 0
                if nl < nr: return -1
                if nl > nr: return 1
            else:
                return 0
            
            
