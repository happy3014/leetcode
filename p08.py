class Solution:
    def _is_digit(self, c):
        return ord('0') <= ord(c) <= ord('9')

    def _char_2_digit(self, c):
        return ord(c) - ord('0')

    def myAtoi(self, s: str) -> int:
        # 对于空字符串，直接返回None
        if not s or not s.strip():
            return 0
        s = s.strip()
        if s[0] == '-':
            symbol = -1
            s = s[1: ]
        elif s[0] == '+':
            symbol = 1
            s = s[1: ]
        elif not self._is_digit(s[0]):
            return 0
        else:
            symbol = 1
        # 没有数字位，直接返回None
        if len(s) == 0:
            return 0
        
        max_number = 2**31 - 1
        min_number = -2**31

        result = 0
        for i in s:
            if not self._is_digit(i):
                break
            result = result * 10 + self._char_2_digit(i) * symbol
            if result <= min_number:
                return min_number
            if result >= max_number:
                return max_number
        return result

if __name__ == '__main__':
    solution = Solution()
    s = '-+43'
    r = solution.myAtoi(s)
    print(r)
            
        

    