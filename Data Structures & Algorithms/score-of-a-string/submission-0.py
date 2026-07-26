class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        score = 0

        for i in range(n - 1):
            abs_sum = abs(ord(s[i]) - ord(s[i+1]))
            score = score + abs_sum

        return score