class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr=s.strip().split(" ")
        count=len(arr[len(arr)-1])
        return count
        