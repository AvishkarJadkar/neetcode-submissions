class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = x
        reverse = 0

        while x > 0:
            lastdigit = x % 10
            reverse = reverse * 10 + lastdigit
            x = x // 10
        return original == reverse
