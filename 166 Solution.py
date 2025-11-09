class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        # Handle zero numerator
        if numerator == 0:
            return "0"
        
        # Handle simple cases where denominator is ±1
        if denominator in {1, -1}:
            return str(numerator * denominator)
        
        # Determine the sign
        negative = (numerator < 0) ^ (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)
        
        # Integer part
        integer_part = str(numerator // denominator)
        remainder = numerator % denominator
        
        # If no fractional part
        if remainder == 0:
            return '-' + integer_part if negative else integer_part
        
        # Fractional part computation
        remainder_positions = {remainder: 0}
        fraction_digits = []
        repeating = False
        position = 0
        
        while remainder != 0:
            position += 1
            remainder *= 10
            digit = remainder // denominator
            fraction_digits.append(str(digit))
            remainder %= denominator
            
            if remainder in remainder_positions:
                repeating = True
                break
            remainder_positions[remainder] = position
        
        # Construct fractional string
        if repeating:
            start = remainder_positions[remainder]
            fraction_digits.insert(start, '(')
            fraction_digits.append(')')
        
        fraction_str = ''.join(fraction_digits)
        result = integer_part + '.' + fraction_str
        return '-' + result if negative else result
