class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=[ch.lower() for ch in s if ch.isalnum()]
        return n==n[::-1]