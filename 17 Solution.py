class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []

        keypad = { '2':['a','b','c'],
                    '3':['d','e','f'],
                    '4':['g','h','i'],
                    '5':['j','k','l'],
                    '6':['m','n','o'],
                    '7':['p','q','r','s'],
                    '8':['t','u','v'],
                    '9':['w','x','y','z']
                   }
        res = keypad[digits[0]]
        digits = list(digits[1:])

        for D in digits:
            new_res = []
            for C in keypad[D]:
                new_res.extend([  res[i]+C for i in range(len(res))  ])
            res = new_res

        return res
