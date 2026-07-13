class Solution:
    def reverse(self, x: int) -> int:
        count = 0
        reverse = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:
            lastdigit = x % 10
            #overflow condition
            if reverse > (2**31-1) // 10:
                return 0
            
            if reverse == (2**31-1) // 10 and lastdigit > 7:
                return 0

            reverse = reverse * 10 + lastdigit
            x = x // 10
        return sign * reverse