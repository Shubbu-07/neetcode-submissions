class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.split()
        s1 = "".join(ch for ch in s)
        s2 = "".join(c for c in s1 if c.isalnum())
        rev = s2[::-1]
        return s2.lower() == rev.lower()