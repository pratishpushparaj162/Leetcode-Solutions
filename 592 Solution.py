import math
import re

class Solution:
    def fractionAddition(self, exp: str) -> str:
        frac_list = re.split(r'(?=[+-])', exp)

        num_list = []
        denom_list = []

        for f in frac_list:
            if f == "":
                continue
            num, denom = f.split('/')
            num_list.append(int(num))
            denom_list.append(int(denom))

        d = math.prod(denom_list)

        for i in range(len(denom_list)):
            num_list[i] = (d // denom_list[i]) * num_list[i]

        n = sum(num_list)
        g = math.gcd(n, d)
        return f"{n//g}/{d//g}"
