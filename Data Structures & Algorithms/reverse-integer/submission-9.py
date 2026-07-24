class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        reverse_number = 0

        while x > 0:
            lastdigit = x % 10
            reverse_number = reverse_number * 10 + lastdigit

            #overflow condition
            
            if reverse_number > (2**31-1) // 10:
                return 0
            
            if reverse_number == (2**31-1) // 10 and lastdigit > 7:
                return 0

            x = x // 10

        return sign * reverse_number

        2147483647
