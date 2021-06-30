class Solution:
    UNITS_MAP = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
    TENS_MAP = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
    HUNDREDS_MAP = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
    THOUSANDS_UNIT = 'M'
    
    def intToRoman(self, num: int) -> str:
        result = []

        thousands_num = int(num / 1000)
        if thousands_num > 0:
            result.append(self.THOUSANDS_UNIT*thousands_num)
        num = num % 1000

        hundreds_num = int(num / 100)
        if hundreds_num > 0:
            result.append(self.HUNDREDS_MAP[hundreds_num])
        num = num % 100

        tens_num = int(num / 10)
        if tens_num:
            result.append(self.TENS_MAP[tens_num])
        num = num % 10

        if num > 0:
            result.append(self.UNITS_MAP[num])
        
        return ''.join(result)


def log(input_str, result):
    print(f'{input_str} -> {result}')       

if __name__ == '__main__':
    solution = Solution()
    inputs = [3, 4, 9, 58, 1994]
    for i in inputs:
        result = solution.intToRoman(i)
        log(str(i), str(result))

