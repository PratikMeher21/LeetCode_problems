class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        result = []

        k -= 1

        fact = 1
        for i in range(1, n):
            fact *= i

        while nums:
            index = k // fact
            result.append(nums[index])
            nums.pop(index)

            if nums:
                k %= fact
                fact //= len(nums)

        return "".join(map(str, result))