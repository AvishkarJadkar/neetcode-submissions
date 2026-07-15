#overflow condition -(2**31) <= x <= (2**31-1)

class Solution:
    def reverse(self,x:int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        rev_num = 0

        while x > 0:
            lastdigit = x % 10
            

            #overflow check
            if rev_num > (2**31-1) // 10:
                return 0
            
            if rev_num == (2**31-1) // 10 and lastdigit > 7:
                return 0

            rev_num = rev_num * 10 + lastdigit
            x = x // 10
        return sign * rev_num
