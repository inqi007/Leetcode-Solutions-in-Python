class Solution:
    def isPalindrome(self, s: str) -> bool:
        plain = ""
        for i in s:
            if i.isalnum():
                plain += i.lower()
        left = 0
        right = len(plain) - 1
        while left <= right:
            if plain[left] == plain[right]:
                left += 1
                right -= 1
            else:
                return False
        return True