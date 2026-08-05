class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0

        while left <= len(haystack) - len(needle):

            right = left
            r = 0

            while r < len(needle) and haystack[right] == needle[r]:
                right += 1
                r += 1

            if r == len(needle):
                return left
                
            left += 1
        return -1
        