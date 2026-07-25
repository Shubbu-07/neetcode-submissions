class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s.split()
        n = len(s)
        word = s[n-1]

        lengthOfLatWord = len(word)
        return lengthOfLatWord