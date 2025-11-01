from functools import cache
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        opens = closes = 0
        runlength = [] #run_length_encoded

        for c in s:
            if runlength and c == runlength[-1][0]:
                runlength[-1][1] += 1
            else:
                runlength.append([c,1])
            if c== ")":
                closes += 1
            elif c=="(":
                opens += 1
            else:
                continue
            
            if closes > opens:
                closes = opens
        
        expected = closes
        
        @cache
        def generate(i, opens, closes):
            if closes > opens or closes > expected or opens > expected:
                return []
            elif i >= len(runlength):
                if opens == closes == expected:
                    return [""]
                else:
                    return []
            else:
                res = []
                ch, w = runlength[i]
                if ch == "(":
                    for j in range(w+1): #
                        res.extend(["("*j + x for x in generate(i+1, opens + j, closes) ])
                elif ch == ")":
                    for j in range(w+1): #
                        res.extend([")"*j + x for x in generate(i+1, opens, closes+j)])
                else:
                    res.extend([ch*w + x for x in generate(i+1, opens, closes)])
                return res

        res = generate(0, 0, 0)
        return res





            




