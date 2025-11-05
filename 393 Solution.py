class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        output = []
        for point in data:
            output.append("".join([str(i) for i in bin(point)[2:].zfill(8)]))
        output = "".join(output)
        idx = 0
        if len(output) < 5:
            return False
        
        def process(output, state):
            if len(output) > 32:
                return False
            elif state == 1:
                return output[0] == '0'
            elif state == 2:
                condition1 = output[-8:-6] == "10"
                condition2 = output[0:3] == '110'
                return condition1 and condition2
            elif state == 3:
                condition1 = output[-8:-6] == "10"
                condition2 = output[-16:-14] == '10'
                condition3 = output[:4] == '1110'
                return condition1 and condition2 and condition3
            else:
                condition1 = output[-8:-6] == "10"
                condition2 = output[-16:-14] == '10'
                condition3 = output[-24:-22] == '10'
                condition4 = output[:5] == '11110'
                return condition1 and condition2 and condition3 and condition4
            return False

        state = 1
        while idx < len(output):
            if idx + 5 < len(output) and idx+32 <= len(output) and output[idx:idx+5] == "11110":
                state = 4 
                valid_data = output[idx:idx+32]
                tmp = process(valid_data, state)
                idx += 32
            elif idx + 4 < len(output) and idx+24 <= len(output) and output[idx:idx+4] == "1110":
                state = 3
                valid_data = output[idx:idx+24]
                tmp = process(valid_data, state)
                idx+=24
            elif idx + 3 < len(output) and idx+16 <= len(output) and output[idx:idx+3] == "110":
                state = 2
                valid_data = output[idx:idx+16]
                tmp = process(valid_data, state)
                idx += 16
            elif idx < len(output) and idx + 8 <= len(output) and output[idx:idx + 1] == '0':
                state = 1
                valid_data = output[idx:idx+8]
                tmp = process(valid_data, state)
                idx += 8
            else:
                return False
            if tmp == False:
                return False
        return True
