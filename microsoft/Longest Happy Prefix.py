class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        for i in range(n - 2, -1, -1):
            prefix = s[:i + 1]
            suffix = s[n - len(prefix):]
            if prefix == suffix:
                return prefix
        return ''
       
