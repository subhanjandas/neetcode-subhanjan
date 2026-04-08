class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        return sum(values[c] if i == len(s) - 1 or values[c] >= values[s[i + 1]] else -values[c] for i, c in enumerate(s))
         