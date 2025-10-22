class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        val_dict = dict(zip(vals,syms))

        solution = ""
        for val in vals:#value_list[::-1]:
            letter_count = num//val #floor division number times it goes in
            if letter_count!=0: 
                solution+= val_dict[val]*letter_count
                num = num-val*letter_count
        return solution

        
